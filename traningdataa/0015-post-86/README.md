# [실습예제] SMC75 개발보드 활용예제

[원본 게시물](https://www.tms320f28x.co.kr/board/view.php?bdId=traningdataa&sno=86) · 활용예제 15번 · 이전일 2026-11-03

SFTP 원본 파일을 수정 없이 보관했습니다. 설치 프로그램은 실행하지 않았습니다. 사용 조건은 원본 배포 자료를 따릅니다.

| 파일 | bytes | SHA-256 |
| --- | ---: | --- |
| [SyncWorks_BLDC_Sensored_281x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_281x.zip) | 5,436,146 | `25ca29078a3c6ec4c592f9d57f832c2bf9fc95c9ff2f6e40195d276fcda54b2e` |
| [SyncWorks_BLDC_Sensored_280x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_280x.zip) | 6,844,265 | `0a8c0d3ac2f32aac18c871fddfaf9db4b44dda5ae2677fc512449765325c7d8d` |
| [SyncWorks_BLDC_Sensored_2833x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_2833x.zip) | 7,106,486 | `a8f86eb31517ca392c85c1d93dac0a69bed70123209b964c3b2a900c68616b6d` |
| [SyncWorks_BLDC_Sensored_281x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_281x_CCSv4.zip) | 6,595,842 | `98121759c604f7858deee1b9853438c658cd07ac5d19d1073ac39e92be679721` |
| [SyncWorks_BLDC_Sensored_280x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_280x_CCSv4.zip) | 8,003,475 | `8d01599961dabb6769b116614eb177f3293fb635a6169251b7d68ffa4fc13c30` |
| [SyncWorks_BLDC_Sensored_2833x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensored_2833x_CCSv4.zip) | 8,280,459 | `f560f59e947f1fd948090d15646e958c043e4129e84c4c698e9fdd6ca5cacdb9` |
| [SyncWorks_BLDC_Sensorless_281x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_281x.zip) | 6,196,984 | `9ebf59090cc1a21be26e46a67661610678f1b8eef8bbf9dee8e0de95a8f896ee` |
| [SyncWorks_BLDC_Sensorless_280x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_280x.zip) | 7,603,962 | `a34e0110000974506b2289c0ea34c09f238e294da6bc035b992f0b5a740dd506` |
| [SyncWorks_BLDC_Sensorless_2833x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_2833x.zip) | 7,879,741 | `7a982dc219199d68eeb45e3540738a99c693a5d87d7b4971bc414dc7074c0ec7` |
| [SyncWorks_BLDC_Sensorless_281x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_281x_CCSv4.zip) | 7,420,112 | `a6bded79ec07c05b032a95959fdf7b3451eb72bc6fd733add8a2533227c25bf5` |
| [SyncWorks_BLDC_Sensorless_280x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_280x_CCSv4.zip) | 8,827,632 | `70bb48871a04d3cca547a5e3ea369726d01ba67b0d5d0446ca8eee710512cabf` |
| [SyncWorks_BLDC_Sensorless_2833x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_BLDC_Sensorless_2833x_CCSv4.zip) | 9,106,836 | `717a297d3e9f0f5fcdcec8b012183c9c1929d15220eba1411c334decae263e29` |
| [SyncWorks_PMSM_Sensored_281x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_281x.zip) | 7,021,628 | `8a83fbc08e09ef0dc62342851a0b1f9a2248d640173ad7e0eb641dbe44c2cb5b` |
| [SyncWorks_PMSM_Sensored_280x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_280x.zip) | 7,065,289 | `2206472be30aec3b87c09ac9d846ca17a65db3652b6a1384576f74727d0bbf6f` |
| [SyncWorks_PMSM_Sensored_2833x.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_2833x.zip) | 8,620,248 | `c04f5c37494b3bf781c27e3593f12a6130e34ae3682022749be7ac4e420269aa` |
| [SyncWorks_PMSM_Sensored_281x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_281x_CCSv4.zip) | 8,320,031 | `3dd99659d227d16f12ceeb4fb991872a208340d21b4873747040690bc4aebe63` |
| [SyncWorks_PMSM_Sensored_280x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_280x_CCSv4.zip) | 8,363,827 | `175c78f3b53c4f4e1f913aeaa4e65a623a73262e20c5e75000f0a1936a11abaf` |
| [SyncWorks_PMSM_Sensored_2833x_CCSv4.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0015-post-86/SyncWorks_PMSM_Sensored_2833x_CCSv4.zip) | 9,935,366 | `d9825f5b47ddf1dfcc6d9cc28431ec4025ddd5ce9990172434f007359b130ccc` |
