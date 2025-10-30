import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# 设置页面标题
st.title("第二重要极限可视化工具")
st.subheader(r"$\lim_{n \to \infty} (1+\frac{1}{n})^n = e$")

# 让用户在线输入正整数n
user_n = st.number_input("请输入正整数n", min_value=1, step=1, value=10)


# 绘图逻辑（和之前一致，适配Streamlit）
def plot_limit(n):
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False

    x = np.linspace(0.1, n, 1000)
    y = (1 + 1 / x) ** x
    e_line = np.full_like(x, np.e)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color='#2E86AB', linewidth=2.5, label=r'$f(x) = (1+\frac{1}{x})^x$')
    ax.plot(x, e_line, color='#A23B72', linestyle='--', linewidth=2, label=f'$e ≈ {np.e:.6f}$')

    n_value = (1 + 1 / n) ** n
    ax.scatter(n, n_value, color='#F18F01', s=80, zorder=5, label=f'$n={n}$ 时的值: {n_value:.6f}')

    ax.set_xlabel('自变量 x (n)', fontsize=12)
    ax.set_ylabel('函数值', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(2, 3)
    return fig


# 点击按钮生成图像
if st.button("生成可视化图像"):
    fig = plot_limit(user_n)
    st.pyplot(fig)