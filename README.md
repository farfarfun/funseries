# funseries

一些小型算法实验的集合仓库，目前只有素数相关的实验代码。

- `funseries.experiment.prime` —— 素数判定与生成：
  - `is_prime(n)` —— 递归试除法判断素数。
  - `is_prime2(n, trials=10)` —— Miller-Rabin 概率素性测试。
  - `prime_generate(max_size=10, max_value=None)` —— 生成指定数量的素数列表。

## 安装

```bash
uv sync
```

## 最小示例

```python
from funseries.experiment.prime import is_prime, prime_generate

assert is_prime(97)
print(prime_generate(max_size=5, max_value=20))
```

输出：`[2, 3, 5, 7, 11]`。

使用 `uv run pytest` 运行测试。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
