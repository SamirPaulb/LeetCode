# Gold Mine Problem
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a gold mine called&nbsp;<strong>M</strong>&nbsp;of (<strong>n x&nbsp;m)</strong> dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner can start from any row in the first column. From&nbsp;a given cell, the miner can move </span></p>

<ol>
	<li><span style="font-size:18px">to the cell diagonally up towards the right&nbsp;</span></li>
	<li><span style="font-size:18px">to the right</span></li>
	<li><span style="font-size:18px">to the cell&nbsp;diagonally down towards the right</span></li>
</ol>

<p><span style="font-size:18px">Find out maximum amount of gold which he can collect.</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 3, m = 3
M = {{1, 3, 3},
     {2, 1, 4},
     {0, 6, 4}};
<strong>Output:</strong> 12
<strong>Explaination:</strong> 
The path is {(1,0) -&gt; (2,1) -&gt; (2,2)}.</span></pre>

<p><br>
<strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 4, m = 4
M = {{1, 3, 1, 5},
     {2, 2, 4, 1},
     {5, 0, 2, 3},
     {0, 6, 1, 2}};
<strong>Output:</strong> 16
<strong>Explaination:</strong> 
The path is {(2,0) -&gt; (3,1) -&gt; (2,2) 
-&gt; (2,3)} or {(2,0) -&gt; (1,1) -&gt; (1,2) 
-&gt; (0,3)}.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>maxGold()</strong> which takes the values n, m and the mine M as input parameters and returns the maximum amount of gold that can be collected.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n*m)<br>
<strong>Expected Auxiliary Space:</strong> O(n*m)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n, m ≤ 50<br>
0 ≤ M[i][j] ≤ 100</span></p>
</div>