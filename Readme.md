# uplay_install.manifest reverse engineering

It seems no one has reverse engineered the Ubisoft Connect/UPlay API, and I have a feeling the `uplay_install.manifest` file is the first step.

## Manifest file structure

| Location    | Size (Bytes)   | Description                                                                        |
|-------------|----------------|------------------------------------------------------------------------------------|
| 0x00000000A | 1              | Major version indicator, generally increments by one with the game's major version |
| 0x00000000C | 344            | Base64 encoded signature key (256-byte when decoded)                               |
| 0x00000164  | through to end | GZIP compressed manifest protobuf data                                             |

The protobuf can be extracted from the manifest by just stripping the first 356 bytes, and unzipping it.

## Protobuf schema

The protobuf schema isn't public. It also can't be pulled from the Ubisoft Connect EXEs because they are packed with VMProtect. However, it is possible to dump the memory of the running Uplay application to extract its protos.

1. Open Ubisoft Connect, then run the below command to dump the memory (it will be about 500 MB)

    ```shell
    # Run CMD/PowerShell as administrator
    procdump64.exe -ma upc.exe
    ```

1. Setup [pbtk](https://github.com/marin-m/pbtk). You won't need the UI (qt) stuff, and it's recommended to install the python dependencies in [pipenv](https://pipenv.pypa.io/en/latest/).

1. Run the binary proto extractor on the memory dump

    ```shell
    pipenv run python3 extractors/from_binary.py upc.exe_210524_171240.dmp upc_protos
    ```

1. Grab the .protos that pbtk spits out into a bunch of folders and copy them to this project. You can ignore the Google protos.

    ```shell
    cp -r upc_protos/*/*.proto ~/my/dir/foo/.
    ```

1. Convert the protos to python code with `protoc`

    ```shell
    protoc --python_out=./classes ./protos/*.proto
    ```

## Findings

The biggest find that I expected to see was a relationship between the download requests made in Ubisoft Connect and a value in the manifest. That can be seen in this Watch Dogs: Legion download request:

`GET http://uplaypc-s-ubisoft.cdn.ubi.com/uplaypc/downloads/3515/slices_v3/d/4D6EB1E526D38615545462D425D723CD53EA6C51
        ?_tkn_=exp=1621790115
        ~acl=/uplaypc/downloads/3515/slices_v3/d/4D6EB1E526D38615545462D425D723CD53EA6C51
        ~data=e0ef48e3-1a89-419e-80c8-a008ef16379a
        ~hmac=8ac6adf9e358dde281c067425a5782a9f90ff57169e9cdbb5494fc48fba07dda`

The value of `4D6EB1E526D38615545462D425D723CD53EA6C51` in the URL can be found in the manifest (`files/wdl_uplay_install.manifest.json`) as base64 (`TW6x5SbThhVUVGLUJdcjzVPqbFE=`) as a file part for `bin\BattlEye\BEClient_x64.dll`. This is a first step to understanding how files are obtained from the UPlay CDN.
