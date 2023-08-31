<h2><a href="https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1">The Painter's Partition Problem-II</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Dilpreet wants to paint&nbsp;his dog's home that has&nbsp;<strong>n</strong> boards with&nbsp;different lengths. The length of i<sup>th&nbsp;</sup>board is given by <strong>arr[i]</strong> where <strong>arr[]</strong> is an array of <strong>n</strong> integers. He hired <strong>k</strong> painters for this work and each painter takes <strong>1 unit time to paint 1 unit of the board.&nbsp;</strong></span></p>

<p><span style="font-size:18px">The problem is to find the minimum time to get this job done if all painters start together with the constraint&nbsp;that any painter will only paint continuous boards, say boards numbered <strong>{2,3,4} </strong>or only board <strong>{1}</strong> or nothing but not boards <strong>{2,4,5}</strong>.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 5
k = 3
arr[] = {5,10,30,20,15}
<strong>Output:</strong> 35
<strong>Explanation: </strong>The most optimal way will be:
Painter 1 allocation : {5,10}
Painter 2 allocation : {30}
Painter 3 allocation : {20,15}
Job will be done when all painters finish
i.e. at time = max(5+10, 30, 20+15) = 35</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 4
k = 2
arr[] = {10,20,30,40}
<strong>Output: </strong>60
<strong>Explanation: </strong>The most optimal way to paint:
Painter 1 allocation : {10,20,30}
Painter 2 allocation : {40}
Job will be complete at time = 60</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your task:</strong><br>
Your task is to complete the function <strong>minTime() </strong>which takes the integers&nbsp;<strong>n </strong>and&nbsp;<strong>k</strong>&nbsp;and the array&nbsp;<strong>arr[]</strong>&nbsp;as input and returns the minimum time required to paint all partitions.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n log m) , m = sum of all boards' length<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤ 10<sup>5</sup><br>
1 ≤ k ≤ 10<sup>5</sup><br>
1 ≤ arr[i] ≤ 10<sup>5</sup></span></p>
</div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<code>Google</code>&nbsp;<code>Codenation</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Divide and Conquer</code>&nbsp;<code>Binary Search</code>&nbsp;<code>Algorithms</code>&nbsp;