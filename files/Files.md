# Sample files

These are just some different versions of the manifest files generated throughout my investigation.

* \<game\>_uplay_install.manifest
  * Just the vanilla `uplay_install.manifest` for the respective game. This file is the same for all players.
* \<game\>_uplay_install.manifest.pb
  * The extracted protobuf payload from the uplay_install.manifest. This is created in `run.py`
* \<game\>_uplay_install.manifest.pb.parsed
  * The `\<game\>_uplay_install.manifest.pb` generated with `protoc --decode_raw`
  * `protoc --decode_raw < files/wd1_uplay_install.manifest.pb > files/wd1_uplay_install.manifest.pb.parsed`
* \<game\>_uplay_install.manifest.json
  * The output of the `\<game\>_uplay_install.manifest.pb` being parsed by the protobuf schema and converted to json. This is created in `run.py`
