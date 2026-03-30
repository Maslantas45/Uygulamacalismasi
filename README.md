# mystery_module.py

## Amaç
Bu modül, ikinci dereceden (quadratic) denklemlerin köklerini hesaplamak için bir fonksiyon içerir. Fonksiyon, verilen katsayılar ile ax² + bx + c = 0 denkleminin reel köklerini döndürür.

## Fonksiyonlar

### fn_x(a, b, c)
- **Açıklama:**
  - ax² + bx + c = 0 biçimindeki ikinci dereceden denklemin köklerini hesaplar.
  - Reel kök yoksa `None` döner.
  - Reel kökler varsa, iki kökü bir tuple olarak döndürür.
- **Parametreler:**
  - `a` (float/int): x²'nin katsayısı
  - `b` (float/int): x'in katsayısı
  - `c` (float/int): sabit terim
- **Dönüş:**
  - `None` (reel kök yoksa)
  - `(x1, x2)` (reel kökler)
- **Kullanım:**
```python
from mystery_module import fn_x

result = fn_x(1, -3, 2)  # x^2 - 3x + 2 = 0
print(result)  # (2.0, 1.0)
```

## Örnekler

- `fn_x(1, 2, 1)` → (-1.0, -1.0)
- `fn_x(1, 0, -4)` → (2.0, -2.0)
- `fn_x(1, 0, 4)` → None (çünkü reel kök yok)

## Notlar
- Fonksiyon yalnızca reel kökleri döndürür. Diskriminant (b²-4ac) negatifse, kök yoktur ve `None` döner.
- a = 0 için (doğrusal denklem) desteklenmez, fonksiyonun davranışı tanımsızdır.

## Gereksinimler
- Python 3.x
- Standart kütüphane (math)
