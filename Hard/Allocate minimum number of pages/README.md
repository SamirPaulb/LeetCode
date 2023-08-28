<h2><a href="https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1">Allocate minimum number of pages</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You have <strong>N</strong> books, each with <strong>Ai</strong> number of pages. <strong>M</strong> students need to be allocated contiguous books, with each student getting at least one book. Out of all the permutations, the goal is to find the permutation where the student with the most <strong>books </strong>allocated to him gets the minimum number of pages, out of all possible permutations.</span></p>
<p><span style="font-size: 18px;"><strong>Note</strong>: Return <strong>-1</strong> if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).</span></p>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 4
A[] = {12,34,67,90}
M = 2
<strong>Output:</strong>113
<strong>Explanation:</strong>Allocation can be done in 
following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages =113.
Therefore, the minimum of these cases is 113,
which is selected as the output.</span></pre>
<p><br><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 3
A[] = {15,17,20}
M = 2
<strong>Output:</strong>32
<strong>Explanation: </strong>Allocation is done as
{15,17} and {20}</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete the function findPages() which takes 2 Integers <strong>N</strong>, and m and an array <strong>A[]</strong> of length <strong>N</strong> as input and returns the expected answer.</span></p>
<p><br><span style="font-size: 18px;"><strong>Expected Time Complexity</strong>: O(NlogN)<br><strong>Expected Auxilliary Space:</strong> O(1)</span></p>
<p><br><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>5</sup><br>1 &lt;= A [ i ] &lt;= 10<sup>6</sup><br>1 &lt;= M &lt;= 10<sup>5</sup></span></p>
<p>&nbsp;</p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Infosys</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Google</code>&nbsp;<code>Codenation</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Divide and Conquer</code>&nbsp;<code>Algorithms</code>&nbsp;