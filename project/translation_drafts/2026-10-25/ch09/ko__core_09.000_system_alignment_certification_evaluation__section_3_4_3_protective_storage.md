<!-- AI-assisted translation draft; unreviewed. §3.4.3 protective storage and key custody, source lines 684–691; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.3 protective storage and key custody (ko)

## English source (lines 684–691)

##### 3.4.3 Protective Storage and Key Custody

For data in the restricted-by-default and non-accessible bands, certification must verify that the system meets the protective storage and key-custody minimum in [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). The record must show:
- where restricted data and its keys actually sit, including backups, caches, logs, and swap;
- that plaintext is confined to the processes that need it; and
- that audit, export, and lawful-override paths still work.

A claim of encryption without that evidence does not satisfy this check.

## Translation draft

##### 3.4.3 보호 저장 및 키 관리

기본적으로 제한되고 접근 불가능한 밴드의 데이터에 대해 인증은 시스템이 [CS-6.305 Part A §5.0 접근 상태 밴드](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands)의 보호 저장 및 키 관리 최소 요건을 충족하는지 확인해야 한다. 기록에는 다음이 나타나야 한다.

- 제한 데이터와 그 키가 백업, 캐시, 로그, 스왑을 포함해 실제로 어디에 있는지;
- 평문이 이를 필요로 하는 프로세스에만 한정되는지; 그리고
- 감사, 반출, 적법한 오버라이드 경로가 계속 작동하는지.

이러한 증거 없이 암호화되어 있다고 주장하는 것만으로는 이 점검을 충족하지 못한다.
