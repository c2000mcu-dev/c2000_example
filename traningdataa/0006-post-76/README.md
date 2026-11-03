# [실습예제] SMC150 개발보드 활용예제 (BLDCM/PMSM,TMS320F28069포함)

[원본 게시물](https://www.tms320f28x.co.kr/board/view.php?bdId=traningdataa&sno=76) · 활용예제 6번 · 이전일 2026-11-03

SFTP 원본 파일을 수정 없이 보관했습니다. 설치 프로그램은 실행하지 않았습니다. 사용 조건은 원본 배포 자료를 따릅니다.

| 파일 | bytes | SHA-256 |
| --- | ---: | --- |
| [TIDCS_SMC150_V2.0.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/TIDCS_SMC150_V2.0.zip) | 6,266,336 | `4721c7727a49635bfdb8faa1f9c1788ae3f343854b6a22da29355d4d00053a46` |
| [SMC150_BLDCM_Sensored_V2.1.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/SMC150_BLDCM_Sensored_V2.1.zip) | 966,533 | `c60a5a3173891130f7490fd565899890694c8f417fd03ce49a0a3e9ebe99dc7a` |
| [SMC150_PMSM_Sensored(FOC)_V2.2.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/SMC150_PMSM_Sensored%28FOC%29_V2.2.zip) | 1,135,133 | `bc501b55310ceb3feb2313b8d13841bd5537f3df92409de9b8b2511ee2d35569` |
| [Hall-Effect Sensor를 이용한 3상 BLDCM의 속력제어 (V2.0).pdf](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/Hall-Effect%20Sensor%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%9C%203%EC%83%81%20BLDCM%EC%9D%98%20%EC%86%8D%EB%A0%A5%EC%A0%9C%EC%96%B4%20%28V2.0%29.pdf) | 3,020,136 | `c4a37c0301362b844c70ac6e4c4272e5924da7b1e7d071486e39b344ef7b29a7` |
| [BLDCM(B60Q-H24051-D5) 사양 및 활용안내.pdf](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/BLDCM%28B60Q-H24051-D5%29%20%EC%82%AC%EC%96%91%20%EB%B0%8F%20%ED%99%9C%EC%9A%A9%EC%95%88%EB%82%B4.pdf) | 515,170 | `a04b052f46ea3089ee18fbb9372ffd46388509c91114a1fce726096643ad26d5` |
| [Incremental Encoder를 이용한 3상 PMSM의 속도, 위치제어 (V2.0).pdf](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/Incremental%20Encoder%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%9C%203%EC%83%81%20PMSM%EC%9D%98%20%EC%86%8D%EB%8F%84%2C%20%EC%9C%84%EC%B9%98%EC%A0%9C%EC%96%B4%20%28V2.0%29.pdf) | 4,301,222 | `aefcdf3b841cec6c0da31180db1a1e16af364d4b5aa1389c93c0cc1f9300e163` |
| [TIDCS_SMC150_V1.5.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/TIDCS_SMC150_V1.5.zip) | 8,367,588 | `6ee1ccfb92105b9af1ab65ac95456defad941b88384e7b880a2957d8ba4f95f1` |
| [SMC150_BLDCM_Sensored_V1.5.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/SMC150_BLDCM_Sensored_V1.5.zip) | 1,591,350 | `8b7405bb85d668f6b480f4842ddc05538faf092fcb639053dd02f9fcb7015879` |
| [SMC150_PMSM_Sensored(FOC)_V1.5.zip](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/SMC150_PMSM_Sensored%28FOC%29_V1.5.zip) | 2,073,018 | `db23e4360daeebbfe1ede1e29bf093f53f18a356e9b034c73cdb7452df7bc696` |
| [Hall-Effect Sensor를 이용한 3상 BLDCM의 속력제어 (V1.5).pdf](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/Hall-Effect%20Sensor%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%9C%203%EC%83%81%20BLDCM%EC%9D%98%20%EC%86%8D%EB%A0%A5%EC%A0%9C%EC%96%B4%20%28V1.5%29.pdf) | 1,332,567 | `0b85771e3b470b99dfb79d9ab3d8055b83aea135824ef1595dd2ebbdc79302ad` |
| [Incremental Encoder를 이용한 3상 PMSM의 속도, 위치제어 (V1.5).pdf](https://github.com/c2000mcu-dev/c2000_example/raw/refs/heads/main/traningdataa/0006-post-76/Incremental%20Encoder%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%9C%203%EC%83%81%20PMSM%EC%9D%98%20%EC%86%8D%EB%8F%84%2C%20%EC%9C%84%EC%B9%98%EC%A0%9C%EC%96%B4%20%28V1.5%29.pdf) | 1,864,916 | `500b1b0ca5a08c98e3bfa6a0473f25f04a31b6ed2128986d67b7824cb0374429` |
