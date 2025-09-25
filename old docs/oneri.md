# ADE Kurallarını İyileştirme ve Yapılandırma Önerileri

Bu doküman, mevcut `rules/*.md` dosyalarını, `awesome-rules` projesinden alınan ilhamla, yapay zeka geliştirme ortamları (ADE'ler) için daha modüler, keşfedilebilir ve etkili bir formata getirme üzerine öneriler sunmaktadır.

## Mevcut Durum Analizi

- **`rules/*.md` dosyaları:** Geniş konuları (kod kalitesi, güvenlik vb.) içeren monolitik (tek parça) dosyalardır. Her dosya, ilgili kategoriye ait birden fazla kuralı barındırır.
- **`awesome-rules` yapısı:** Her bir kuralın kendi `.md` dosyasına sahip olduğu oldukça granüler (parçalı) bir yapıya sahiptir. `rules.json` manifest dosyaları, bu kuralları programatik olarak keşfedilebilir kılar.

## İdeal Yapı İçin Öneriler

Temel amaç, monolitik dosyaları parçalayarak her kuralı tek başına bir birim haline getirmek ve bu kuralları bir manifest sistemiyle yönetmektir.

---

### Öneri 1: Granüler Kural Dosyaları (Tek Sorumluluk Prensibi)

Her kural kendi markdown dosyasına ayrılmalıdır. Bu, bir ADE'nin belirli bir göreve odaklanırken yalnızca ilgili kuralı yüklemesini sağlar, bu da verimliliği ve doğruluğu artırır.

**Mevcut Durum:**
```
rules/01-code-quality-en.md (içinde 5+ kural var)
```

**Önerilen Durum:**
```
rules/
└───01-code-quality/
    ├─── readability.md
    ├─── simplicity-kiss.md
    ├─── consistency.md
    ├─── refactoring.md
    └─── commenting.md
```

**Faydası:** Yapay zeka, "kod okunabilirliğini artır" gibi bir görev aldığında, sadece `readability.md` dosyasının içeriğine odaklanabilir. Bu, bağlamı daraltır ve daha isabetli sonuçlar üretir.

---

### Öneri 2: Kategori Bazlı Manifest Dosyaları (`rules.json`)

Her kural kategorisi (örneğin `01-code-quality/`), içinde hangi kuralların olduğunu listeleyen bir `rules.json` manifest dosyası içermelidir. Bu, `awesome-rules` yapısındaki en güçlü özelliklerden biridir.

**Önerilen `01-code-quality/rules.json` İçeriği:**
```json
[
  {
    "id": "readability",
    "name": "Code Readability and Clarity",
    "description": "Code should be written to be easily understandable by other developers.",
    "documentation": "readability.md",
    "tags": ["clean-code", "readability"]
  },
  {
    "id": "simplicity-kiss",
    "name": "Simplicity and Conciseness (KISS)",
    "description": "Prefer simple, straightforward solutions over complex ones.",
    "documentation": "simplicity-kiss.md",
    "tags": ["clean-code", "kiss-principle"]
  }
]
```

**Faydası:** Bu yapı, bir ADE'nin "kod kalitesiyle ilgili tüm kuralları listele" veya "`clean-code` etiketine sahip kuralları bul" gibi komutları anında ve verimli bir şekilde çalıştırmasını sağlar. Sistem, `.md` dosyalarını tek tek taramak yerine bu JSON dosyalarını okur.

---

### Öneri 3: Birleşik ve Ölçeklenebilir Dizin Yapısı

Önceki iki öneriyi birleştirerek temiz, hiyerarşik ve kolayca genişletilebilir bir ana dizin yapısı oluşturulmalıdır.

**Önerilen Dizin Yapısı:**
```
rules/
├───01-code-quality/
│   ├─── rules.json
│   ├─── readability.md
│   └─── simplicity-kiss.md
├───02-docs-ui/
│   ├─── rules.json
│   ├─── comprehensive-docs.md
│   └─── clear-ui-text.md
├───03-error-testing/
│   ├─── rules.json
│   ├─── principled-error-handling.md
│   └─── multi-layered-testing.md
└─── ... (diğer kategoriler)
```

**Faydası:** Bu yapı, projenin büyümesini kolaylaştırır. Yeni bir kural kategorisi eklemek, sadece yeni bir dizin ve ilgili dosyaları oluşturmak kadar basit hale gelir.

---

### Öneri 4: Kök Manifest Dosyası (Opsiyonel ama Güçlü)

Tüm kural setini tek bir noktadan keşfedilebilir kılmak için `rules/` dizininin köküne tüm kategorileri listeleyen bir `manifest.json` eklenebilir.

**Önerilen `rules/manifest.json` İçeriği:**
```json
{
  "name": "ADE Development Rules",
  "version": "1.0.0",
  "description": "A comprehensive set of rules to help ADEs write better code.",
  "categories": [
    {
      "id": "01-code-quality",
      "name": "Code Quality",
      "path": "01-code-quality/rules.json"
    },
    {
      "id": "02-docs-ui",
      "name": "Documentation and UI/UX",
      "path": "02-docs-ui/rules.json"
    }
  ]
}
```

**Faydası:** Bir ADE veya araç, sisteme entegre olurken sadece bu tek dosyayı okuyarak tüm kural hiyerarşisini ve mevcut tüm kuralları öğrenebilir. Bu, sistemin başlatılması (bootstrapping) için son derece verimli bir yöntemdir.

## Sonuç

Bu öneriler, mevcut `rules` koleksiyonunu, modern ve otomatize geliştirme araçlarının tam potansiyelinden yararlanabileceği, son derece yapılandırılmış ve verimli bir formata dönüştürecektir. Bu dönüşüm, kuralların sadece insanlar tarafından değil, aynı zamanda yapay zeka tarafından da etkin bir şekilde anlaşılmasını ve uygulanmasını sağlayacaktır.