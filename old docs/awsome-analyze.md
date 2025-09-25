# `awesome-rules` Yapısının Detaylı Analizi

Bu doküman, `awesome-rules` projesinin dosya ve dizin yapısını, çalışma mantığını ve bileşenlerinin nasıl etkileşimde bulunduğunu detaylı bir şekilde açıklamaktadır. Analiz, proje içinde iki farklı kural tanımlama yapısı olduğunu ortaya koymuştur.

## 1. Genel Yapı

Proje, kuralları kategorilere ayrılmış modüler bir yapıda saklar. Ana dizin olan `awesome-rules-main/rules/` altında her bir kural kategorisi için ayrı bir alt dizin bulunur.

Örnek Dizin Yapısı:
```
awesome-rules-main/
└───rules/
    ├───clean-code/      # Yapı Tipi 1
    │   ├───rules.json
    │   ├───check-code-quality.md
    │   └───solid.md
    ├───api-docs/        # Yapı Tipi 2
    │   ├───rules.json
    │   ├───api-docs-copywriting.md
    │   └───openapi-standards.md
    └───... (diğer kategoriler)
```

## 2. Kural Yapısı Tipleri

Proje içerisinde iki temel `rules.json` formatı tespit edilmiştir.

---

### Yapı Tipi 1: Manifest Tabanlı Kategori (Örn: `clean-code`)

Bu yapıda, `rules.json` dosyası kategori içindeki tüm kuralları açıkça listeleyen bir "manifest" (bildirim) dosyası görevi görür.

**`clean-code/rules.json` Örneği:**
```json
[
  {
    "id": "check-code-quality",
    "name": "Check Code Quality",
    "description": "A rule to check the quality of the code.",
    "documentation": "check-code-quality.md"
  },
  {
    "id": "check-solid",
    "name": "Check SOLID Principles",
    "description": "A rule to check if the code follows SOLID principles.",
    "documentation": "check-solid.md"
  }
]
```

- **İşlevi:** Bir otomasyon aracının, o kategorideki kuralları (ID, isim, açıklama) ve ilgili dokümanları (`.md` dosyaları) doğrudan keşfetmesini sağlar.
- **Bileşenler:**
    - **`id`:** Kural için benzersiz programatik tanımlayıcı.
    - **`name`:** Kuralın insan tarafından okunabilir adı.
    - **`description`:** Kuralın kısa özeti.
    - **`documentation`:** Detaylı açıklamayı içeren `.md` dosyasının yolu.

---

### Yapı Tipi 2: Meta Veri Odaklı Kategori (Örn: `api-docs`, `cicd`)

Bu yapıda, `rules.json` dosyası bireysel kuralları listelemek yerine, kategorinin kendisine ait genel meta verileri içerir.

**`api-docs/rules.json` Örneği:**
```json
{
  "name": "api-docs/openapi-rules",
  "description": "Best practices for API documentation and OpenAPI standards",
  "version": "0.0.1",
  "author": "API Documentation Team",
  "tags": ["api", "documentation", "openapi", "swagger", "rest"]
}
```

- **İşlevi:** Kategoriyi bir bütün olarak tanımlar. Bu yapıdaki kurallar, `rules.json` dosyasında listelenmek yerine, dizin içindeki `.md` dosyalarının varlığıyla dolaylı olarak tanımlanır.
- **Bileşenler:**
    - **`name`:** Kategorinin adı.
    - **`description`:** Kategorinin genel açıklaması.
    - **`tags`:** Kategoriyi sınıflandırmak için kullanılan etiketler.

## 3. Çalışma Mantığı ve İş Akışı

`awesome-rules` yapısını kullanan bir sistemin her iki yapıyı da desteklemesi gerekir:

1.  **Kural Keşfi (Discovery):** Araç, `awesome-rules-main/rules/` altındaki her bir kategori dizinini tarar.
2.  **Yapı Tipi Tespiti:** Her dizindeki `rules.json` dosyasının içeriğini okur.
    - **Eğer içerik bir JSON dizisi ise (Array `[...]`):** Bunu **Yapı Tipi 1** olarak kabul eder. Dizideki her bir nesneyi ayrı bir kural olarak işler ve `documentation` alanından `.md` dosyasına ulaşır.
    - **Eğer içerik bir JSON nesnesi ise (Object `{...}`):** Bunu **Yapı Tipi 2** olarak kabul eder. Kategorinin meta verisini bu nesneden alır. Kural listesini oluşturmak için dizin içindeki tüm `.md` dosyalarını listeler (örneğin `api-docs-copywriting.md`, `openapi-standards.md`). Dosya adları kural ID'leri olarak kullanılabilir.
3.  **Birleşik Kural Listesi:** Her iki yöntemle elde edilen kuralları birleştirerek sistemdeki tüm kuralların tam bir listesini oluşturur.
4.  **Detay Sunumu:** Kullanıcı bir kuralın detayını istediğinde, ilgili `.md` dosyasının içeriğini okur ve sunar.

## Sonuç

Bu çift yapı, projenin esnekliğini gösterse de, kuralları işleyecek bir aracın her iki senaryoyu da yönetebilecek şekilde tasarlanması gerektiğini göstermektedir. Yapı Tipi 1 daha açık ve programatikken, Yapı Tipi 2 daha az yapılandırılmış ve dosya sistemi taramasına dayalıdır.
