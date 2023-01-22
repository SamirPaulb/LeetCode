<h2><a href="https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/">2546. Apply Bitwise Operations to Make Strings Equal</a></h2><h3>Medium</h3><hr><div><p>You are given two <strong>0-indexed binary</strong> strings <code>s</code> and <code>target</code> of the same length <code>n</code>. You can do the following operation on <code>s</code> <strong>any</strong> number of times:</p>

<ul>
	<li>Choose two <strong>different</strong> indices <code>i</code> and <code>j</code> where <code>0 &lt;= i, j &lt; n</code>.</li>
	<li>Simultaneously, replace <code>s[i]</code> with (<code>s[i]</code> <strong>OR</strong> <code>s[j]</code>) and <code>s[j]</code> with (<code>s[i]</code> <strong>XOR</strong> <code>s[j]</code>).</li>
</ul>

<p>For example, if <code>s = "0110"</code>, you can choose <code>i = 0</code> and <code>j = 2</code>, then simultaneously replace <code>s[0]</code> with (<code>s[0]</code> <strong>OR</strong> <code>s[2]</code> = <code>0</code> <strong>OR</strong> <code>1</code> = <code>1</code>), and <code>s[2]</code> with (<code>s[0]</code> <strong>XOR</strong> <code>s[2]</code> = <code>0</code> <strong>XOR</strong> <code>1</code> = <code>1</code>), so we will have <code>s = "1110"</code>.</p>

<p>Return <code>true</code> <em>if you can make the string </em><code>s</code><em> equal to </em><code>target</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "1010", target = "0110"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "<strong><u>0</u></strong>0<strong><u>1</u></strong>0".
- Choose i = 2 and j = 1. We have now s = "0<strong><u>11</u></strong>0".
Since we can make s equal to target, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "11", target = "00"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make s equal to target with any number of operations.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length == target.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>target</code> consist of only the digits <code>0</code> and <code>1</code>.</li>
</ul>
</div>