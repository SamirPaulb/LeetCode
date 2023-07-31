<h2><a href="https://leetcode.com/problems/surrounded-regions">130. Surrounded Regions</a></h2><h3>Medium</h3><hr><p>Given an <code>m x n</code> matrix <code>board</code> containing <code>&#39;X&#39;</code> and <code>&#39;O&#39;</code>, <em>capture all regions that are 4-directionally&nbsp;surrounded by</em> <code>&#39;X&#39;</code>.</p>

<p>A region is <strong>captured</strong> by flipping all <code>&#39;O&#39;</code>s into <code>&#39;X&#39;</code>s in that surrounded region.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 550px; height: 237px;" />
<pre>
<strong>Input:</strong> board = [[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;O&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;O&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;X&quot;,&quot;X&quot;]]
<strong>Output:</strong> [[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;X&quot;,&quot;X&quot;,&quot;X&quot;],[&quot;X&quot;,&quot;O&quot;,&quot;X&quot;,&quot;X&quot;]]
<strong>Explanation:</strong> Notice that an &#39;O&#39; should not be flipped if:
- It is on the border, or
- It is adjacent to an &#39;O&#39; that should not be flipped.
The bottom &#39;O&#39; is on the border, so it is not flipped.
The other three &#39;O&#39; form a surrounded region, so they are flipped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = [[&quot;X&quot;]]
<strong>Output:</strong> [[&quot;X&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is <code>&#39;X&#39;</code> or <code>&#39;O&#39;</code>.</li>
</ul>
