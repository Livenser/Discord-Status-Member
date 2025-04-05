<div style="font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 20px;">
  <h2 style="text-align: center;">💻 Cara Setup Discord Status Member Bot</h2>
  <p style="text-align: center;">Langkah-langkah ini gampang banget, cocok buat lu yang baru mau nyoba atau udah punya bot sendiri.</p>

  <ol>
    <li>
      <strong>Lu harus punya bot Discord dulu</strong><br>
      Kalau belum punya, langsung aja bikin di <a href="https://discord.com/developers/applications" target="_blank">Discord Developer Portal</a>.  
      Kalo udah, lanjut ke langkah berikutnya.
    </li>
    <br>
    <li>
      <strong>Download code-nya dalam bentuk ZIP</strong><br>
      Klik tombol "Code" di GitHub terus pilih "Download ZIP". Setelah itu, extract file-nya kayak biasa.
    </li>
    <br>
    <li>
      <strong>Buka folder project di VSCode atau editor kesayangan lu</strong><br>
      Masuk ke folder <code>status</code> yang udah diextract tadi. Buka aja langsung dari editor yang biasa lu pake, contohnya VSCode.
    </li>
    <br>
    <li>
      <strong>Edit file <code>.env</code></strong><br>
      Di dalam folder itu, cari file <code>.env</code>, terus masukin token bot Discord lu ke situ. Contohnya:
      <pre><code>DISCORD_BOT_TOKEN=isi_token_bot_discord_lu_disini</code></pre>
    </li>
    <br>
    <li>
      <strong>Jalankan file <code>main.py</code></strong><br>
      Sekarang tinggal buka terminal, terus jalanin:
      <pre><code>python main.py</code></pre>
      Kalau Semuanya benar, Selamat bot lu akan memiliki status untuk member server lu.
    </li>
    <br>
    <li>
      <strong>Selamat! 🎉</strong><br>
      Bot lu sekarang udah punya fitur slash command. Gampang kan? Tinggal dijalanin aja.
    </li>
  </ol>
