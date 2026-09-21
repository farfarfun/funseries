#!/usr/bin/env bash
# 使用 uv 构建并检查 funseries。
set -euo pipefail

case "${1:-}" in
  build) uv build ;;
  install) uv sync ;;
  test) uv run pytest ;;
  *) printf '用法：%s {build|install|test}\n' "$0" >&2; exit 1 ;;
esac
