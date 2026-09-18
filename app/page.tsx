import Image from "next/image";

const xUrl = "https://x.com/MEMORIELA_JP";

const topics = [
  { date: "2026.09.16", title: "久遠ゆら 公式ビジュアル公開" },
  { date: "2026.09.17", title: "MEMORIELA 公式サイト公開" },
];

const developmentHistory = [
  { date: "2026.09.11", title: "ゆらの公式ビジュアルを正式決定", text: "久遠ゆらの公式ビジュアルを確定。" },
  { date: "2026.09.06", title: "チャットUI実装", text: "専用Desktop会話UI、画像入力・認識、Relationship永続管理、音声基盤更新を実装。" },
  { date: "2026.08.30", title: "ゆらの人格・自発性を強化", text: "ゆら自身の人格や状態を会話に反映する仕組みを拡張。自分から話しかける機能、Web検索、眠気による状態変化を実装。" },
  { date: "2026.08.23", title: "記憶と感情の仕組みを実装", text: "長期記憶、Relationship、複合感情、音声表現の基盤を実装。" },
  { date: "2026.08.16", title: "久遠ゆら、誕生", text: "Project YURA始動。AIとしての会話・音声機能の最初の基盤を実装。" },
];

export default function Home() {
  return (
    <main>
      <header className="header">
        <a className="brand" href="#home" aria-label="MEMORIELA home">
          <Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={520} height={260} priority />
        </a>
        <nav aria-label="Main navigation">
          <a href="#project">Project.YURA</a>
          <a href="#technology">Technology</a>
          <a href="#gallery">Gallery</a>
          <a href="#history">History</a>
        </nav>
        <a className="officialX" href={xUrl} target="_blank" rel="noreferrer" aria-label="Official X">𝕏</a>
      </header>

      <section className="hero" id="home">
        <div className="heroVisual">
          <Image src="/images/yura-dress.png" alt="久遠ゆら / YURA" fill priority sizes="100vw" />
        </div>
        <div className="heroShade" />
        <div className="heroBrand">
          <p>MEMORIELA</p>
          <span>Memory shapes personality.</span>
        </div>
        <aside className="topics" aria-label="Latest topics">
          <div className="topicsHead"><span>LATEST</span><b>TOPICS</b></div>
          {topics.map((item) => (
            <article key={item.date + item.title}>
              <time>{item.date}</time>
              <p>{item.title}</p>
            </article>
          ))}
        </aside>
      </section>

      <section className="project section" id="project">
        <div className="sectionTitle">
          <span>PROJECT</span>
          <h2>Project.YURA</h2>
          <p>久遠ゆら</p>
        </div>
        <div className="projectLayout">
          <div className="projectVisual placeholderVisual">
            <Image src="/images/yura-dress.png" alt="久遠ゆら / YURA" fill sizes="45vw" />
          </div>
          <div className="profileCard">
            <p className="eyebrow">KUON YURA</p>
            <h3>久遠 ゆら</h3>
            <p className="profileLead">AIと、心が通う物語。</p>
            <div className="profileLines">
              <span>PROFILE</span>
              <span>Project.YURA</span>
              <span>MEMORIELA</span>
            </div>
            <p className="placeholderNote">プロフィールと自己紹介は、実画面を確認しながらここへ追加します。</p>
          </div>
        </div>
      </section>

      <section className="technology section" id="technology">
        <div className="sectionTitle centered">
          <span>CONCEPT & TECHNOLOGY</span>
          <h2>記憶が、人格を形作る。</h2>
        </div>
        <div className="technologyGrid">
          <article><b>01</b><h3>Memory</h3><p>記憶</p></article>
          <article><b>02</b><h3>Personality</h3><p>人格</p></article>
          <article><b>03</b><h3>Relationship</h3><p>関係性</p></article>
        </div>
        <p className="sectionPlaceholder">Technology / Concept の説明は、公開範囲を確認しながら次の工程で詰めます。</p>
      </section>

      <section className="gallery section" id="gallery">
        <div className="sectionTitle centered">
          <span>CHARACTER VISUAL</span>
          <h2>Gallery</h2>
        </div>
        <div className="galleryGrid">
          <figure className="galleryMain"><Image src="/images/yura-dress.png" alt="久遠ゆら official visual" fill sizes="60vw" /></figure>
          <div className="gallerySlots">
            <div className="gallerySlot"><span>VISUAL 02</span></div>
            <div className="gallerySlot"><span>VISUAL 03</span></div>
          </div>
        </div>
      </section>

      <section className="history section" id="history">
        <div className="sectionTitle centered">
          <span>PROJECT.YURA</span>
          <h2>Development History</h2>
          <p>開発履歴</p>
        </div>
        <div className="timeline">
          {developmentHistory.map((item) => (
            <article key={item.date}>
              <time>{item.date}</time>
              <i aria-hidden="true" />
              <div><h3>{item.title}</h3><p>{item.text}</p></div>
            </article>
          ))}
        </div>
      </section>

      <footer id="official">
        <div className="footerBrand">
          <Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={520} height={260} />
          <p>Memory shapes personality.</p>
        </div>
        <div className="footerLinks">
          <a href="#project">Project.YURA</a>
          <a href={xUrl} target="_blank" rel="noreferrer">Official X</a>
          <span>YouTube</span>
        </div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}
