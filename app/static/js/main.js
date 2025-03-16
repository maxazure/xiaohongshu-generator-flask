/**
 * 小红书图片生成器主JavaScript文件
 */

// 在DOM加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 自动关闭提示框
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            // 获取bootstrap的alert对象并调用关闭方法
            const bsAlert = new bootstrap.Alert(alert);
            setTimeout(function() {
                bsAlert.close();
            }, 3000); // 3秒后关闭
        });
    }, 500);

    // 初始化提示框
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 确认删除操作
    const deleteButtons = document.querySelectorAll('[data-action="delete"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('确定要删除这个帖子吗？此操作不可逆。')) {
                e.preventDefault();
            }
        });
    });

    // 返回顶部按钮
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', function() {
            if (document.documentElement.scrollTop > 200) {
                scrollToTopBtn.style.display = 'block';
            } else {
                scrollToTopBtn.style.display = 'none';
            }
        });

        scrollToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // 支持复制链接功能
    const copyLinkBtns = document.querySelectorAll('.copy-link-btn');
    copyLinkBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const url = this.getAttribute('data-url');
            navigator.clipboard.writeText(url)
                .then(() => {
                    // 成功时显示提示
                    const originalText = this.innerHTML;
                    this.innerHTML = '已复制!';
                    setTimeout(() => {
                        this.innerHTML = originalText;
                    }, 1500);
                })
                .catch(err => {
                    console.error('复制失败: ', err);
                });
        });
    });

    // 手机预览交互增强
    const phoneContainer = document.querySelector('.phone-container');
    if (phoneContainer) {
        // 添加长按保存图片提示
        phoneContainer.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            alert('提示: 在实际应用中，您可以长按图片保存。');
        });

        // 双击点赞动画
        phoneContainer.addEventListener('dblclick', function() {
            const heart = document.createElement('div');
            heart.classList.add('heart-animation');
            heart.innerHTML = '❤️';
            heart.style.position = 'absolute';
            heart.style.top = '50%';
            heart.style.left = '50%';
            heart.style.transform = 'translate(-50%, -50%)';
            heart.style.fontSize = '80px';
            heart.style.opacity = '0';
            heart.style.transition = 'all 0.6s ease';
            heart.style.zIndex = '100';
            
            phoneContainer.appendChild(heart);
            
            setTimeout(() => {
                heart.style.opacity = '1';
                heart.style.fontSize = '120px';
            }, 10);
            
            setTimeout(() => {
                heart.style.opacity = '0';
            }, 600);
            
            setTimeout(() => {
                phoneContainer.removeChild(heart);
            }, 1200);
        });
    }
});

// Markdown预览功能
function updateMarkdownPreview(content, previewElement) {
    if (!previewElement) return;
    
    fetch('/api/markdown-render', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: content })
    })
    .then(response => response.json())
    .then(data => {
        previewElement.innerHTML = data.html;
    })
    .catch(error => {
        console.error('预览更新失败:', error);
        previewElement.innerHTML = '<div class="alert alert-danger">预览加载失败</div>';
    });
}
