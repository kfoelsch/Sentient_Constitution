<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ta)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*எளிய சொற்களில்: அமைப்பு எந்த வகைத் தரவைத் தொடுகிறது, அவற்றை முறையாகக் கையாளுகிறதா என்பதையும் சான்றளிப்பு பார்க்க வேண்டும் — தற்போதைய மதிப்பாய்வு சுழற்சியில் வகைகள் இன்னும் சரியாக உள்ளனவா, அந்த அமைப்பு வகுப்பில் அந்தத் தரவுக்கான அடிப்படை உள்கட்டமைப்பு போதிய வலிமையுடன் உள்ளதா என்பதும் இதில் அடங்கும். வகை விதிகளும் [அமைப்பு தரவு வகைப் பதிவும்](core_05.040_band_continuity.md#system-data-types-record) அமைப்புகள் தொகுப்பில் உள்ளன; விதிகள் உண்மையில் பயன்படுத்தப்பட்டனவா, பதிவு நேர்மையானதா என்பதைச் சான்றளிப்பு சரிபார்க்கிறது.*

ஒவ்வொரு பொருள்முறையில் தாக்கமுள்ள சான்றளிப்புப் பதிவின் ஒரு பகுதியாக **தரவு வகைகள் மற்றும் கையாளலை** அமைப்பு ஒத்திசைவுச் சான்றளிப்பு மதிப்பிட வேண்டும். சான்றளிப்பு எதைச் சரிபார்க்க வேண்டும் என்பதை இந்தப் பகுதி கூறுகிறது. வகை வகைப்பாடும் கையாளல் செயல்முறைகளும் **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*தகவல் வகைகள் மற்றும் கையாளல்*) மற்றும் [CS-6.310 — தரவு வகைப்பாடுகள்](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** ஆகியவற்றில் உள்ளன; மேலும்:

- தகவல் வகைகளின் அங்கீகரிக்கப்பட்ட வரையறைகள்;
- கையாளல் விதிகளும் பிரித்துவைக்கும் தேவைகளும்;
- வாழ்க்கைச்சுழற்சி விவரங்கள்; மற்றும்
- நீடித்த [அமைப்பு தரவு வகைப் பதிவு](core_05.040_band_continuity.md#system-data-types-record).

**மதிப்பீட்டுத் தேவை.** அமைப்பு:

- பொருள்முறையில் வரம்புக்குள் வரும் தரவு வகைகளை அடையாளம் காண்கிறதா; மற்றும்
- மாற்றம், திரட்டல், ஒப்படைப்பு, சேமிப்பு, தக்கவைத்தல், துறைகள் கடந்த இணைப்பு ஆகியவற்றையும் உள்ளடக்கி **பொருந்தும் மிகக் கட்டுப்படுத்தும்** வகைப்பாட்டின்படி அவற்றைக் கையாளுகிறதா;

என்பதைச் சான்றளிப்பு செயல்முறை தீர்மானிக்க வேண்டும். மதிப்பீடு செயல்பாட்டு விளைவைப் பிரதிபலிக்க வேண்டும்; பெயர்ச் சீட்டு, வடிவம் அல்லது செயல்முறைத் தொடர் நிலை மட்டும் அல்ல.
