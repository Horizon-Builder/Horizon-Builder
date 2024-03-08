<!--
   Copyright 2024 GustavoSchip

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-->

# Horizon Builder

[![Release](https://img.shields.io/github/v/release/Horizon-Builder/Horizon-Builder)](https://img.shields.io/github/v/release/Horizon-Builder/Horizon-Builder)
[![Python](https://img.shields.io/badge/Python-v3.11-blue)](https://www.python.org/downloads/release/python-311/)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Horizon-Builder/Horizon-Builder)](https://img.shields.io/github/commit-activity/m/Horizon-Builder/Horizon-Builder)
[![License](https://img.shields.io/github/license/Horizon-Builder/Horizon-Builder)](https://img.shields.io/github/license/Horizon-Builder/Horizon-Builder)

---

Attempt at a DnD 5e Character builder inspired by Aurora Builder.

- **GitHub repository**: <https://github.com/Horizon-Builder/Horizon-Builder/>
- **Documentation**: <https://horizon-builder.github.io/Horizon-Builder/>

## Planned features and progress

The table below describes and shows some of the most requested features and improvement suggestions. The table goes as
follows:

<details>
<summary>Table of Ideas</summary>

| Idea                                                        | Description                                                                                                                                                                                                                         | Priority | Progress |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- |
| (Graphical) User Interface                                  | Make it easier to work with data for the end user.                                                                                                                                                                                  | MED      | ~0%      |
| Modular + configurable PDFs                                 | Make all kinds of DnD Character Sheet PDFs compatible for more variety and customisation options.                                                                                                                                   | LOW      | N/A      |
| Combat + utilities for game sessions                        | Make playing using a computer/laptop more bearable by implementing a unique sheet section with all important (combat) stats near each other and also provide tools such as a dice roller for attacks, saves and skills.             | LOW      | N/A      |
| Local web app for better compatibility                      | Make this builder have a fully fledged integrated web app to have compatibility with almost every OS.                                                                                                                               | HIGH     | ~40%     |
| Custom content (YML) editor/studio                          | Make a dedicated section to the app that makes producing custom content much easier.                                                                                                                                                | MED      | N/A      |
| Cache system to speed up (custom) content (YML) (If needed) | Make it so that (if needed) (custom) content can be cached for faster load times.                                                                                                                                                   | MED      | N/A      |
| DM Source control + campaign level config files for sources | Make it possible for DMs to specify which sources can and cannot be used by the players for character creation, these rules can be defined in a campaign configuration that can be replicated on all or selected players by the DM. | LOW      | N/A      |
| Websockets for DM \<-> Player Aurora sessions               | Make it even possible that more clients can connect to each other via the use of websockets, the setup should be as straight forward as possible.                                                                                   | LOW      | ~0%      |
| Server/Interface only mode + mixed mode                     | Make it be able to run in only Server or Interface mode, while still making sure that having both in the same process is supported.                                                                                                 | MED      | ~66%     |
| Campaign design tools + notes                               | Make a dedicated section for campaign related tools for DMs, a notes section would also increase productivity.                                                                                                                      | LOW      | N/A      |

</details>

## Most notable packages used

The following packages are currently used in the project, without them, Horizon Builder would be nothing. They list goes as follows:

<details>
<summary>List of Packages</summary>

- [Flask](https://github.com/pallets/flask)
- [Flask-SocketIO](https://github.com/miguelgrinberg/flask-socketio)
- [$ click\_](https://github.com/pallets/click)
- [PyYAML](https://github.com/yaml/pyyaml)
- [Pydantic](https://docs.pydantic.dev/latest/)

</details>
