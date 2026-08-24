# BẢN TRÍCH HÀM VẼ — HH7_CH03 — tự sinh từ `hinh_gocdt.py`

> **Cho AI Soạn.** Đây là *CÁCH vẽ* (chữ ký hàm + tham số). *VẼ CÁI GÌ* nằm ở **phiếu khai nghĩa** Ông Bụt giao kèm nguồn.
> Tự sinh bằng introspect `hinh_gocdt.py` qua `sinh_bantrich.py` — vá kho → chạy lại → khớp. KHÔNG sửa tay file này.
> Sinh ngày 24/08/2026. Mô hình (X): OB khai nghĩa → AI Soạn GỌI HÀM theo phiếu → PHANH kiểm.

Import trong script bài: `import hinh_gocdt as H3` rồi `h = H3.Hinh()`.
Gọi các method KHAI NGHĨA (mục 1) theo phiếu; cuối cùng `png = h.ve(out=..., tra_bytes=True)`.

---

## 1. HÀM KHAI NGHĨA — AI Soạn GỌI theo phiếu

Mỗi hàm nhận NGHĨA (tên đỉnh/tia, số đo, loại quan hệ). Máy tự tính tọa độ + PHANH kiểm.

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `cat_tuyen_2duong(a='a', b='b', c='c', A='A', B='B', song_song=True, xoay_ab=8, xoay_c=108, khoang=1.9, danh_so=True, nhan_dinh=True, danh_dau_ss=False, rut_c_tren=0.5, dai=2.2)` | Cát tuyến c cắt đường a (trên) tại A và đường b (dưới) tại B. song_song=True → a // b (PHANH kiểm). xoay_ab: nghiêng chung a,b; xoay_c: nghiêng c. khoang: khoảng dọc giữa a và b. danh_so → A1–A4 tại A, B1–B4 tại B (phần tư). danh_dau_ss: mặc định TẮT (đường thẳng không đặt dấu trên đường); bật khi bài cần nhấn ký hiệu song song. rut_c_tren: tỉ lệ GIỮ LẠI của nhánh cát tuyến c PHÍA TRÊN A (mặc định 0.5 = cắt bỏ nửa phần thò lên trên A cho gọn; đặt 1.0 để giữ nhánh trên dài như nhánh dưới). |
| `chum_duong(tam, danh_sach, dai=3.0)` | CHÙM ĐƯỜNG THẲNG đồng quy tại 'tam'. danh_sach=[(tên, xoay°), …] — mỗi đường qua tâm, nghiêng 'xoay'° so ngang, dài 'dai' về mỗi phía. Nhãn cạnh 1 đầu. Dùng nhiều đường cắt nhau tại 1 điểm. |
| `chum_tia(dinh, danh_sach, cung=None)` | cung=[(canh1,canh2,số_đo), ...] để vẽ + kiểm góc giữa 2 tia. |
| `da_giac_deu(*ten, canh=2.0, xoay=0, to=None)` | Đa giác đều n cạnh (n = số tên truyền vào ≥ 3), đỉnh theo chiều kim đồng hồ, một cạnh nằm ngang phía trên khi xoay=0. Dùng cho hình NHẬN DẠNG / gây nhiễu (ngũ giác, bát giác,…) — KHÔNG vẽ đường chéo. to = màu tô miền (None = không tô). Lục giác đều dùng riêng luc_giac_deu (có đường chéo chính/phụ, tâm). |
| `da_giac_vuong(ten, buoc, nhan='below right')` | Đa giác mọi cạnh song song trục (góc vuông) — hình chữ L, bậc thang, mặt bằng. ten = list tên đỉnh (n đỉnh), đi quanh chu vi. buoc = list n (huong, dai) — huong ∈ {'phai','trai','len','xuong'}, dai>0. Đỉnh sinh cộng dồn từ ten[0]=(0,0); TỔNG vector phải = 0 (khép kín). (Nhãn cạnh/kích thước AI thêm bằng doan(..., dodai=...).) |
| `dau_bang(A, B, so_vach=1, kiem_bang=None)` | Đánh dấu CẠNH BẰNG NHAU trên đoạn A,B (đã đặt) bằng 'so_vach' vạch (1/2/3) — vạch khác nhau phân biệt các NHÓM cạnh bằng khác nhau (dấu ×/×× như SGK 8.33). kiem_bang=khóa nhóm (bất kỳ) → gom mọi đoạn cùng khóa vào PHANH cạnh-bằng (kiểm hình dựng đúng bằng nhau). Chỉ đánh dấu, không tự nối đoạn. |
| `dau_goc_bang(goc, so_gach=1, ban_kinh=7, mau='orange', do=None)` | Đánh dấu GÓC (cung + 'so_gach' gạch tick) → thể hiện HAI GÓC BẰNG NHAU. Các góc bằng nhau (vd 2 nửa của góc bị tia phân giác chia) dùng CÙNG so_gach. goc = (canh1, dinh, canh2) đã đặt. do: số đo thật (None → tự tính từ toạ độ). PHANH kiểm. |
| `dau_song_song(A, B, so_mui=1)` | Đánh dấu HƯỚNG SONG SONG trên đoạn A,B (đã đặt) bằng 'so_mui' mũi tên (1/2) — các đoạn cùng số mũi tên = cùng phương (ký hiệu >/>> như SGK). Chỉ đánh dấu. |
| `diem_giua(ten, A, B, ti_le=0.5, mau=None, nhan='above')` | Điểm 'ten' nằm giữa A,B. ti_le∈(0,1) vị trí tương đối (KHÔNG phải tọa độ). mau='red' → chấm đỏ (điểm dựng ở lời giải). nhan='below' → tên điểm xuống dưới (tránh đè nhãn độ dài đặt phía trên, vd 8.30). |
| `diem_luoi(ten, cot, hang, mau=None)` | Điểm 'ten' tại NÚT (cột,hàng) — chỉ số nguyên, dữ kiện đề (như số đo góc). mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `diem_ngoai(ten, duong, phia=None, mau=None, doc=0.0)` | Điểm 'ten' KHÔNG thuộc 'duong'. phia ∈ {'tren','duoi','trai','phai'}. doc: dời điểm DỌC theo đường (đơn vị vẽ) để đặt nhiều điểm ngoài phân biệt. mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `diem_ngoai_goc(ten, goc, lech=0, xa=1.6, mau=None)` | Điểm 'ten' nằm NGOÀI 'goc' (bộ 3 (cạnh1,đỉnh,cạnh2) đã khai qua goc/chum_tia). Đối xứng với diem_trong: đặt theo hướng PHÂN GIÁC NGOÀI (miền phản xạ) → chắc chắn ngoài góc. lech=số độ xoay hướng ngoài (đặt nhiều điểm ngoài phân biệt; PHANH vẫn kiểm phải nằm ngoài, xoay quá tay vào trong → dừng). xa=khoảng cách từ đỉnh. mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `diem_tren(ten, duong, thu_tu=None, mau=None)` | Điểm 'ten' ∈ 'duong'. thu_tu=số nguyên xếp thứ tự nhiều điểm trên 1 đường. mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `diem_trong(ten, goc, lech=0, xa=1.3, mau=None)` | Điểm 'ten' nằm TRONG 'goc' (bộ 3 (cạnh1,đỉnh,cạnh2) đã khai qua goc/chum_tia). lech=số độ xoay quanh đỉnh so phân giác trong (đặt NHIỀU điểm trong phân biệt; xoay quá tay ra ngoài → PHANH dừng). xa=khoảng cách từ đỉnh. mau='red' → chấm đỏ. |
| `doan(A, B, dodai=None, danh_dau=None, mau=None, net='lien', rong=None)` | Đoạn 2 mút A,B (đã đặt). dodai='4 cm' ghi độ dài. danh_dau='='|số → gạch bằng + kiểm. mau/net: style phân biệt (kết quả lời giải = mau='red', net='lien' → đỏ liền đậm). rong ∈ {'manh','vua','dam','rat_dam'}: bề dày nét — phân biệt vai đoạn (vd kim giờ 'dam' vs kim phút 'manh' trong đồng hồ; None = mặc định theo mau/net). |
| `doan_le(A, B, dai=3.0, dodai=None, huong='ngang', danh_dau=None, mau=None, net='lien')` | ĐOẠN THẲNG ĐƠN LẺ — tự đặt 2 mút A,B rồi vẽ (KHÔNG cần đặt điểm trước). Mút cách nhau 'dai' (đơn vị vẽ) theo 'huong' ∈ {'ngang','doc','cheo'}; 'dodai'='4 cm' ghi độ dài; danh_dau/mau/net như doan(). Nhãn A,B ở 2 đầu. Gọi NHIỀU LẦN → mỗi đoạn tự xuống 1 DÒNG (không chồng), CĂN TRÁI cùng mốc (để mắt so độ dài). Dùng cho hình 'đoạn thẳng có ghi độ dài' (8.25/8.29/8.31). Đoạn đơn không khai quan hệ nào → PHANH không có gì để tái đo (đúng). |
| `duong(ten, nhan2dau=None, mau=None, net='lien', an_nhan=False)` | ĐƯỜNG THẲNG tên 'ten' (d,a,b,m…). nhan2dau=('x','y') → nhãn 2 đầu (đường xy). mau/net: style phân biệt (đường phụ lời giải = mau='red', net='dut'). an_nhan=True → KHÔNG hiện nhãn đường (đường trần, vd bài 'lấy điểm'). |
| `duong_diem(ten, ds_diem, nhan2dau=None, an_nhan=False, mau=None, net='lien', diem_do=())` | ĐƯỜNG THẲNG mang danh sách điểm ĐÃ SẮP THỨ TỰ (trái→phải): rải ĐỀU và CĂN GIỮA; đường TỰ CO vừa các điểm (thò 2 đầu một khoảng cố định). Thay cho duong+diem_tren khi bài là 'các điểm trên một đường' (nhận biết thẳng hàng, tia đối…). nhan2dau=('x','y') → nhãn 2 đầu; an_nhan=True → đường trần; diem_do=[…] → các điểm chấm ĐỎ (điểm dựng ở lời giải). Tự thêm ràng buộc thẳng hàng (PHANH). |
| `duong_qua(A, B, mau='red', net='dut')` | ĐƯỜNG THẲNG (kéo dài 2 phía) qua 2 điểm A,B đã đặt — dùng vẽ ĐƯỜNG PHỤ trong lời giải. Mặc định đỏ nét đứt (quy ước yếu tố dựng thêm). A,B đã được PHANH kiểm qua con đường nghĩa của chúng nên KHÔNG thêm ràng buộc (Đ5.9 vẫn kín). |
| `giao(ten, dt1, dt2, mau=None)` | ĐIỂM 'ten' = giao của 2 đường (tên) HOẶC 2 đoạn (tuple mút). Song song → raise. mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `goc(dinh, canh1, canh2, do, xoay=0, vuong=False, hien_so=True)` | AI Soạn chỉ khai: đỉnh, tên 2 cạnh, số đo. Máy đặt 2 cạnh BẰNG NHAU (DAI_CHUAN), cạnh1 nghiêng 'xoay'° so ngang, cạnh2 = cạnh1 + do. vuong=True → vẽ ô vuông thay cung số. hien_so=False → vẽ cung góc NHƯNG ẩn số đo (hình ĐỀ đo-góc / minh hoạ so sánh: chỉ hiện cung, không lộ đáp án — Đ35). |
| `goc_vuong(ten)` | Đánh dấu GÓC VUÔNG (90°) trên góc 'ten' = (cạnh1, đỉnh, cạnh2) đã khai — vẽ Ô VUÔNG nhỏ thay cung số. PHANH kiểm góc = 90°. Chỉ đánh dấu; 2 cạnh phải khai trước qua tia/chum_tia. |
| `hai_duong(ten1, ten2, quan_he)` | quan_he ∈ {'cat','song_song','trung'}. Máy đặt thỏa quan hệ + PHANH kiểm. |
| `hai_duong_cat_4goc(ten1='xx′', ten2='yy′', O='O', xoay1=10, xoay2=105, danh_so=True, nhan_dinh=True, prefix='', dai=2.2)` | Hai đường thẳng ten1, ten2 cắt nhau tại đỉnh O. xoay1/xoay2: góc nghiêng (độ) của mỗi đường so phương ngang. danh_so=True → đánh số 4 góc theo phần tư I–IV (prefix để ghi 'O' nếu cần). PHANH: O ∈ cả hai đường (buộc 2 đường thực sự cắt tại O). |
| `hinh_thang(A, B, Cc, D, day_tren=3.0, day_duoi=5.0, cao=2.5, lech=0.8)` | Hình THANG thường: A,B = đáy trên (day_tren); D,C = đáy dưới (day_duoi); AB ∥ DC (PHANH song_song). cao = chiều cao; lech = dời ngang đáy trên. Thang CÂN dùng hinh_thang_can. |
| `hinh_thang_can(A, B, Cc, D, day_nho=3.0, day_lon=5.0, cao=2.5, cheo=False)` | Hình thang cân đối xứng qua trục dọc: A,B = đáy nhỏ (trên); D,C = đáy lớn (dưới). A trên-trái, B trên-phải, C dưới-phải, D dưới-trái. cheo=True → vẽ 2 đường chéo (AC, BD — bằng nhau). |
| `hinh_thoi(A, B, Cc, D, canh=3.0, goc=60, cheo=False, tam=None)` | Hình thoi dạng "kim cương": A trái, B trên, C phải, D dưới. canh = độ dài cạnh; goc = góc tại đỉnh A (và C), độ (mặc định 60°). cheo=True → vẽ 2 đường chéo (AC ngang, BD dọc). tam = tên tâm (chấm). |
| `hinh_vuong(M, N, P_, Q, canh=3.0)` | Hình VUÔNG: M dưới-trái, N trên-trái, P trên-phải, Q dưới-phải. canh = độ dài cạnh. PHANH: 4 cạnh bằng nhau + góc tại M vuông (90°). |
| `luc_giac_deu(A, B, Cc, D, E, F, canh=2.0, xoay=0, cheo=None, tam=None)` | Lục giác đều 6 đỉnh, thứ tự A→B→C→D→E→F theo chiều kim đồng hồ. Khi xoay=0: cạnh AB (trên) và ED (dưới) nằm ngang; C ở phải, F ở trái. canh = độ dài cạnh (= bán kính đường tròn ngoại tiếp). xoay = góc xoay cả hình (độ). cheo = None | 'chinh' (AD,BE,CF) | 'phu' (AC,BD,CE,DF,EA,FB) | 'tatca'. tam = tên tâm O (đặt → chấm tâm; 3 đường chéo chính đồng quy tại O). |
| `luoi(cot, hang)` | Lưới nền cot×hang ô (xám nhạt). |
| `nhan_goc(goc, chu, r=0.44)` | Ghi nhãn 'chu' (số thứ tự '1','2','3'… hoặc ký hiệu) tại phân giác TRONG của góc. goc = (canh1, dinh, canh2): tên 3 điểm ĐÃ đặt (qua tia/tia_doi…). Dùng cho các hình đánh số góc KHÔNG theo phần tư liên tục (vd H3.5: Ô₁–Ô₂ đối đỉnh). Không vẽ cung. |
| `noi(*diem, kin=False, mau=None)` | Nối các điểm ĐÃ ĐẶT thành đoạn/gấp khúc. kin=True→đa giác đóng. mau=màu đường. |
| `so_do_goc(ten, do=None, hien_so=True, mau='orange', ban_kinh=7)` | mau/ban_kinh: khi 1 hình có ≥2 cung góc lồng nhau → dùng MÀU KHÁC + bán kính khác để phân biệt (Đ: cung trong nhỏ cam, cung ngoài lớn xanh). do=None → TỰ ĐO từ toạ độ (vẽ cung đánh dấu góc mà không assert số đo cho trước). |
| `tam_giac(A, B, Cc, noi=True)` | Tam giác 3 đỉnh (không thẳng hàng). Thứ tự A→B→C chiều kim đồng hồ. noi=False → chỉ ĐẶT 3 điểm (không nối cạnh) — dùng cho 'ba điểm không thẳng hàng'. |
| `tam_giac_deu(A, B, Cc, canh=3.0, xoay=0)` | Tam giác ĐỀU 3 đỉnh: B dưới-trái, C dưới-phải, A đỉnh trên. canh = độ dài cạnh (mặc định 3.0). Ba cạnh bằng nhau (PHANH canh_bang). Dùng nhận dạng / hình nền. |
| `thang_hang(*diem)` | KHAI các điểm THẲNG HÀNG → PHANH kiểm độ lệch, sai thì dừng. |
| `thuoc_do_goc(dinh, tia0, tia_do, do, xoay=0, chieu=1, ban_kinh=2.5, thang='don')` | THƯỚC ĐO GÓC (nửa đường tròn chia độ) áp lên góc tia0-đỉnh-tia_do — minh hoạ/đọc số đo. tia0 = cạnh trùng vạch 0 (đặt nghiêng 'xoay'° so ngang); tia_do = cạnh chỉ 'do' độ. chieu=+1 quét ngược chiều kim (tia_do phía trên), -1 thuận chiều kim. thang='doi' hai thang 0–180 như SGK (dạy chọn thang), 'don' một thang. Máy đặt 2 tia + phủ thước (vạch chính 10° có số, vạch phụ 2°). PHANH kiểm góc tia0-đỉnh-tia_do = do. |
| `tia(goc_O, ten_dau, xoay=0, mui_ten=False, nhan='auto', mau=None, net='lien')` | TIA gốc 'goc_O' hướng tới 'ten_dau', nghiêng 'xoay'° so ngang (0 = sang phải). Gốc chưa đặt → đặt tại (0,0). mui_ten=True → mũi tên đầu tia (ký hiệu tia). nhan: vị trí nhãn mút ('auto' tự chọn). mau/net: style phân biệt (đường phụ lời giải = 'red'/'dut'). Tia đơn: 1 gốc, 1 hướng. |
| `tia_diem(goc_O, ds, xoay=0, ten_tia=None, hai_dau=False, nhan_dodai=False, mau=None, net='lien')` | TIA gốc 'goc_O' mang các điểm ĐO ĐƯỢC (metric). ds=[(tên, vị_trí), …] · vị_trí = khoảng cách từ gốc theo ĐƠN VỊ BÀI; vị_trí ÂM = điểm trên TIA ĐỐI. Máy chuẩn hoá tỉ lệ, đặt gốc O, vẽ mũi tên đầu dương (hai_dau=True → mũi tên cả hai đầu), ràng buộc thẳng hàng (PHANH). ten_tia: nhãn cạnh mũi tên (vd 'x' cho tia Ox). nhan_dodai=True → ghi khoảng cách từ gốc dưới mỗi điểm. (Song sinh với duong_diem, nhưng cho TIA + vị trí metric.) |
| `tia_doi(O, t1, t2, xoay=0)` | HAI TIA ĐỐI chung gốc O: t1 và t2 hai phía đối nhau qua O, nghiêng 'xoay'° so ngang. Vẽ đoạn t1–t2 + PHANH kiểm góc t1-O-t2 = 180° và t1,O,t2 thẳng hàng. Dùng bài 'hai tia đối nhau'. |
| `to_mien(*diem, mau='cyan!18')` | TÔ MÀU một miền = đa giác qua các điểm ĐÃ ĐẶT (theo thứ tự). Dùng tô: • miền trong 1 góc: to_mien(P1, đỉnh, P2) — P1,P2 trên 2 cạnh; • giao/hợp nhiều góc (miền trong tam giác — 8.30): to_mien(A, B, C). Miền được tô NẰM DƯỚI mọi nét (không che hình). mau: màu tô nhạt. |
| `trung_diem(M, A, B, mau=None)` | M = TRUNG ĐIỂM đoạn AB. M chưa đặt → tự đặt tại chính giữa A,B. Vẽ đoạn AB + gạch bằng 2 nửa (A–M = M–B) + ràng buộc thẳng hàng A,M,B (PHANH). mau='red' → chấm đỏ (điểm dựng ở lời giải). |
| `tu_giac(A, B, Cc, D, loai=None)` | Tứ giác 4 đỉnh lồi, chiều kim đồng hồ. loai∈{None,'binh_hanh','chu_nhat'}. |

## 2. CỬA RENDER

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `ve(out='hinh', tra_bytes=False, nhan=None)` | CỬA RENDER — gọi CUỐI cùng. Chạy PHANH verify (sai hình → DỪNG tại đây) rồi xuất TikZ→PNG. out = tên file (không đuôi). tra_bytes=True → trả bytes PNG (nhúng docx qua template); False → ghi file. nhan = caption "Hình N" nướng CĂN GIỮA DƯỚI ảnh (cho hình neo phải mục ③+). Mọi hàm khai nghĩa phải gọi TRƯỚC ve(). |

## 3. HÀM HẠ TẦNG — máy dùng nội bộ, **AI Soạn KHÔNG gọi**

Các hàm hạ tầng (nhận tọa độ thô hoặc cần điểm đặt trước) do các hàm khai nghĩa ở mục 1 tự gọi bên trong. Theo Đ5.9, người không cho tọa độ → **AI Soạn không gọi trực tiếp nhóm này**. Danh sách đã ẩn khỏi bản trích. Gặp hình mà mục 1 chưa phủ (vd đa giác thường) → **DỪNG báo Ông Bụt bổ sung hàm thuần-nghĩa** (khép vòng A↔C), KHÔNG tự dùng hàm hạ tầng.

---

**Thống kê:** 43 hàm khai nghĩa (phơi) · 1 cửa render · 13 hàm hạ tầng (ẩn khỏi bản phát).

> **Nợ:** kho chưa khai `LOP_MODULE` → bản trích chưa ghi lớp áp dụng.
