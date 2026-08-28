# funseries

一些小型算法实验的集合仓库，目前只有素数相关的实验代码。

- `funseries.experiment.prime` —— 素数判定与生成：
  - `is_prime(n)` —— 递归试除法判断素数。
  - `is_prime2(n, trials=10)` —— Miller-Rabin 概率素性测试。
  - `prime_generate(max_size=10, max_value=None)` —— 生成指定数量的素数列表。

## 安装

```bash
pip install funseries
```
