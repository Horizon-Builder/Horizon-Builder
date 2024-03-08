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

The table below describes and shows some of the most requested features and improvement suggestions. The board goes as
follows:

| Idea                                                                                      | Description                                                                                                                                                                                                             | Priority | Progress |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- |
| (Graphical) User Interface                                                                | Make it easier to work with data for the end user.                                                                                                                                                                      | MID      | 0%       |
| Modular + configurable PDF                                                                | Make all kinds of DnD Character Sheet PDFs compatible for more variety and customisation options.                                                                                                                       | LOW      | N/A      |
| Combat + utilities for game sessions                                                      | Make playing using a computer/laptop more bearable by implementing a unique sheet section with all important (combat) stats near each other and also provide tools such as a dice roller for attacks, saves and skills. | LOW      | N/A      |
| XML content compatibility from [Aurora Builder](https://aurorabuilder.com/documentation/) | Make it so that most (if not all) already made content for Aurora Builder is compatible with Horizon Builder.                                                                                                           | LOW      | 1.5%     |
| Local web app for better compatibility                                                    | Make this builder have a fully fledged integrated web app to have compatibility with almost every OS.                                                                                                                   | HIGH     | 40%      |
| Custom content (YML) editor/studio                                                        | TODO                                                                                                                                                                                                                    | MID      | N/A      |
| Cache system to speed up custom content (YML)                                             | TODO                                                                                                                                                                                                                    | MID      | N/A      |
| DM Source control + campaign level config files for sources                               | TODO                                                                                                                                                                                                                    | LOW      | N/A      |

## Technologies used

The following technologies (packages) are currently used in the project, the technologies listed below are the ones that
are included in the packaged release:

- [defusedxml](https://github.com/tiran/defusedxml)
- [Flask](https://github.com/pallets/flask)
- [$ click\_](https://github.com/pallets/click)
- [PyYAML](https://github.com/yaml/pyyaml)
- [Pydantic](https://docs.pydantic.dev/latest/)
