
hexo.extend.tag.register('postlink', function(args, content) {
  try {
    // 更强大的解析器
    const items = content.split('\n')
      .map(line => line.trim())
      .filter(line => line && !line.startsWith('//'))
      .map(line => {
        // 提取键值对
        const pairs = line.match(/(\w+)\s*:\s*"([^"]+)"/g) || [];
        const data = {};
        pairs.forEach(pair => {
          const [key, value] = pair.split(':').map(s => s.trim().replace(/^"|"$/g, ''));
          if (key && value) data[key] = value;
        });
        return data;
      })
      .filter(item => item.url && item.img);

    if (!items.length) {
      return '';
    }

    return `
<div class="links-content-data">
  ${items.map(item => `
  <div class="links-content-data-item">
    <a target="_blank" rel="noopener" href="https://${item.url}">
      <div class="card">
        <div class="user-link-image">
          <img src="/assets/website/${item.img}" alt="${item.text || 'Link'}" style="margin:0px;">
        </div>
        ${item.text ? `
        <div class="user-link-info">
          <h1 style="font-size:17px;border-bottom:0;margin:0;font-weight:400;">
            ${item.text}
          </h1>
        </div>
        ` : ''}
      </div>
    </a>
  </div>
  `).join('')}
</div>`;
  } catch (e) {
    return `<div style="color:red">Postlink Error: ${e.message}</div>`;
  }
}, {ends: true, async: true});  // 添加 async 选项