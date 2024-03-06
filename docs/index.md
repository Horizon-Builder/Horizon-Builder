<!--
   Copyright [2024] [GustavoSchip]

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

# Gustav-Engine

[![Release](https://img.shields.io/github/v/release/Gustav-Engine/Gustav-Engine)](https://img.shields.io/github/v/release/Gustav-Engine/Gustav-Engine)
[![codecov](https://codecov.io/gh/Gustav-Engine/Gustav-Engine/branch/main/graph/badge.svg?token=ZMQTFLR4RH)](https://codecov.io/gh/Gustav-Engine/Gustav-Engine)
[![Python](https://img.shields.io/badge/Python-v3.11-blue)](https://www.python.org/downloads/release/python-311/)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Gustav-Engine/Gustav-Engine)](https://img.shields.io/github/commit-activity/m/Gustav-Engine/Gustav-Engine)
[![License](https://img.shields.io/github/license/Gustav-Engine/Gustav-Engine)](https://img.shields.io/github/license/Gustav-Engine/Gustav-Engine)

---

Attempt at a DnD 5e Character builder inspired by Aurora Builder.

- **GitHub repository**: <https://github.com/Gustav-Engine/Gustav-Engine/>
- **Documentation**: <https://Gustav-Engine.github.io/Gustav-Engine/>

## Planned features and progress

The table below describes and shows some of the most requested features and improvement suggestions. The board goes as
follows:

| Idea                                                                                      | Description | Priority | Progress |
| ----------------------------------------------------------------------------------------- | ----------- | -------- | -------- |
| (Graphical) User Interface                                                                | TODO        | MID      | N/A      |
| Modular + configurable PDF                                                                | TODO        | LOW      | N/A      |
| Combat + utilities for game sessions                                                      | TODO        | LOW      | N/A      |
| XML content compatibility from [Aurora Builder](https://aurorabuilder.com/documentation/) | TODO        | HIGH     | 1.5%     |
| Local web app for better compatibility                                                    | TODO        | MID      | 0%       |
| Custom content (XML) editor/studio                                                        | TODO        | MID      | N/A      |
| GitHub community guidelines, pull request + issue templates and `**.md` updates           | TODO        | LOW      | 95%      |
| More robust Python versions support                                                       | TODO        | LOW      | -        |
| Cache system to speed up custom content (XML)                                             | TODO        | HIGH     | N/A      |

## Technologies used

The following technologies (packages) are currently used in the project, the technologies listed below are the ones that
are included in the packaged release:

- [defusedxml](https://github.com/tiran/defusedxml)
- [Flask](https://github.com/pallets/flask)
- [$ click\_](https://github.com/pallets/click)
- [PyYAML](https://github.com/yaml/pyyaml)
