### 摘自力扣官方解答，用作参考
#### 简单的方法：
- 从表达式的左侧开始，每次只处理一个括号。
- 假设遇到一个开括号，表达式是否无效取决于在该表达式的其余部分的某处是否有相匹配的闭括号，此时，只是增加计数器的值保持跟踪现在为止开括号的数目。`left += 1`
- 如果遇到一个闭括号，可能意味着两种情况：
1、此闭括号没有与之对应的开括号，这种情况下，表达式无效。当`left==0`，也就是没有未配对的左括号可用时就是这种情况。
2、有一些未配对的开括号可以与改闭括号配对，当`left>0`,也就是有未配对的左括号可用时就是这种情况。