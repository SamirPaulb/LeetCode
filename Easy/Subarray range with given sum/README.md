<h2><a href="https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum0128/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article">Subarray range with given sum</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an unsorted array of&nbsp;integers and a <strong>sum</strong>. The task is to count the number of&nbsp;subarray which adds to the&nbsp;given sum.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 5
arr[] = {10,2,-2,-20,10}
sum = -10
<strong>Output: </strong>3<strong>
Explanation: </strong>Subarrays with sum -10 are: 
[10, 2, -2, -20], [2, -2, -20, 10] and 
[-20, 10].</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 6
arr[] = {1,4,20,3,10,5}
sum = 33
<strong>Output: </strong>1<strong>
Explanation: </strong>Subarray&nbsp;with sum 33 is: 
[20,3,10].</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You only need to complete the function <strong>subArraySum()&nbsp;</strong>that takes <strong>arr, n, sum as parameters</strong> and <strong>returns </strong>the <strong>count&nbsp;</strong>of subarrays which adds up to the given sum.&nbsp;<br>
<br>
<strong>Expected Time Comlexity:&nbsp;</strong>O(n)<br>
<strong>Expected Auxilary Space:&nbsp;</strong>O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n&nbsp;&lt;= 10<sup>5</sup><br>
-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup><br>
-10<sup>5</sup> &lt;= sum &lt;= 10<sup>5</sup></span></p>

<p>&nbsp;</p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;<code>Data Structures</code>&nbsp;