# YURA — Strong-Braided Half-Up Hair Reference

Status: **AUTHOR PASS / APPROVED HAIRSTYLE REFERENCE**  
Author approval: **2026-10-18**

## 1. Approved reference image

`visuals/yura/identity/hair/styles/strong-braided-half-up/YURA_STRONG_BRAIDED_HALF_UP_MASTER.png`

Git `main` に登録された承認画像を、この髪型の正面Face-upリファレンスとする。

- Git blob SHA: `6c8f54781903b2d94ec0a58f3e3ce73df7f4fecb`
- Repository file size: `1,882,562 bytes`

この画像以前の生成候補・修正途中画像を参照元に戻さない。

## 2. Authority scope

本資料は、作者が **strong-braided half-up（編み込みを伴うハーフアップ）** を指定した場合の**髪型専用Authority**である。顔・耳・頭蓋・身体・衣装・背景のAuthorityを上書きしない。

上位・関連Authority:

- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — 最高位Visual Text Authority
- `visuals/yura/identity/face/YURA_FACE_REFERENCE.png`
- `visuals/yura/identity/face/YURA_FACE_UP_MASTER.md`
- `visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md`
- `visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`
- `visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md`
- `visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png` — 全身統合Master

画像内の衣装・背景は髪型Authorityの対象外とする。

## 3. Approved front-view visual description — 髪型の視覚的定義

- 髪色は、明るい**銀白色**。淡い寒色寄りの陰影と繊細な毛束の階調を持ち、暖色ブロンドへ変更しない。
- 前髪は、頭頂付近から額へ自然に落ちる**薄く軽い前髪**。中央付近に細い束の重なりがあり、額は部分的に透ける。重いぱっつん前髪にはしない。
- 頭部の左右上側には、複数の細い毛束が**後方へ向かって編み込まれたように重なり、まとまる**。正面からは側頭部に沿う編み込み状の立体的な毛流れとして見える。
- 上部の毛束を後方へまとめつつ、**下側の長い髪は結わずに残す**ハーフアップ構成とする。左右の下ろした髪は、顔の両側から肩の下へ滑らかに落ちる。
- 顔まわりには細い自然な毛束を残す。顔の外側へ不自然に広げず、前髪・編み込み部分・下ろした髪が連続した髪型として見えるようにする。
- 正面から**結び目・留め位置の全容は確認できない**。画像で確認できない後頭部の厳密な結束位置・編み込み経路・固定具の構造は、新しい確定設定として補完しない。
- 髪飾りを追加しない。画像内の胸元のリボン・花飾りは**衣装の要素**であり、髪飾りの指定ではない。

## 4. View-dependent hairstyle invariants

- カメラから結び目や編み込みの全体が見えなくても正常とする。
- 見せるために結び目を左右へずらす、前方へ回り込ませる、髪の流れを作り替える、頭部形状を変える、といった補正は禁止。
- Face-up画像のトリミングから、実際の毛先全長・身体比率・頭身を推定しない。全身での髪長と身体の整合は上位Authorityに従う。
- **正面・頭を傾けない・真顔・閉口**をFace-up基準とする。髪型変更を理由に顔Geometryや表情を再解釈しない。

## 5. Ear geometry lock — 耳の大型化・長大化を禁止

耳は本髪型画像から新設・再設計しない。実際の耳の大きさ・形状・位置は**Ear Geometry Master**および**Ear Basic Rules**を適用する。

- 耳を**長くしない**。縦方向への引き伸ばし・耳たぶの延長は禁止。
- 耳を**大きくしない**。縦を短くする代わりに横幅を増やす補償も禁止。
- 耳を外側へ押し出さない。正面に向ける、カメラ側へ傾ける、回転させる、頭部から離す補正は禁止。
- 耳の高さのTARGETは**顔の縦寸法の20〜22%**、**HARD MAXは23%**。数値は髪に隠れた部分を含む耳の実Geometryに適用する。
- 耳を見せるため、髪を避けたり、顔まわりの毛束を耳の後ろへ移したり、編み込みを調整したりしない。
- **耳が一部しか見えない／左右の露出が異なる／完全に隠れる状態は正常**とする。左右の見え方を揃える目的で耳のGeometryを変更しない。
- 耳の可視性と自然なサイズが両立しなければ、**自然に髪へ隠れる状態を優先**する。

```text
EAR GEOMETRY > EAR VISIBILITY.
DO NOT ENLARGE OR ELONGATE EARS.
DO NOT ROTATE OR REPOSITION EARS TO MAKE THEM VISIBLE.
HAIR OCCLUSION IS ACCEPTABLE.
DO NOT IMPROVISE YURA'S FACE.
```

## 6. Promotion and usage

作者による髪型画像のPASSは完了。上記のPNGがGit `main` に登録済みであることを確認している。

以後、明示的にこのハーフアップを指定された場合にのみ本髪型Referenceを適用する。その他の髪型・Face/Ear/Body Authorityは変更しない。
