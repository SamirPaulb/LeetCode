<h2><a href="https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1">Boundary Traversal of binary tree</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order:&nbsp;</span></p>

<ol>
	<li><span style="font-size:18px"><strong>Left boundary nodes:</strong>&nbsp;defined as the path from the root to the left-most node&nbsp;</span><span style="font-size:18px">ie- the&nbsp;leaf node you could reach when you always travel preferring&nbsp;the left subtree over the&nbsp;right subtree.&nbsp;</span></li>
	<li><span style="font-size:18px"><strong>Leaf nodes:&nbsp;</strong>All the leaf nodes except for the ones that are part of left or right boundary.</span></li>
	<li><span style="font-size:18px"><strong>Reverse right boundary nodes:</strong>&nbsp;defined as the path from&nbsp;the right-most node to the&nbsp;root. The&nbsp;right-most node is&nbsp;the&nbsp;leaf node you could reach when you always travel preferring&nbsp;the right subtree over the&nbsp;left subtree.&nbsp;Exclude the root from this as it was already included in the traversal of left boundary nodes.</span></li>
</ol>

<p><span style="font-size:18px"><strong>Note:</strong> If the root doesn't have a left subtree or right subtree, then the root itself is the left&nbsp;or right boundary.&nbsp;</span><br>
<br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
        </span></strong><span style="font-size:18px">1 
&nbsp;     /   \
&nbsp;    2     3</span><strong><span style="font-size:18px">&nbsp; 
&nbsp;   </span></strong><span style="font-size:18px">/ \   / \ 
&nbsp;  4   5 6   7
&nbsp;     / \
&nbsp;    8   9</span><strong><span style="font-size:18px">
   
Output: </span></strong><span style="font-size:18px">1 2 4 8 9 6 7 3</span><strong><span style="font-size:18px">
Explanation:
</span></strong><span style="font-size:18px"><strong><img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20211103204119/graph4-300x300.png" style="height:300px; width:300px"></strong></span><strong><span style="font-size:18px">
</span></strong>
</pre>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">            1
           /
          2
        /  \
       4    9
     /  \    \
    6    5    3
             /  \
            7     8
</span><strong><span style="font-size:18px">
Output: </span></strong><span style="font-size:18px">1 2 4 6 5 7 8
<strong>Explanation:
</strong><a href="https://contribute.geeksforgeeks.org/wp-content/uploads/boundary.png"><img alt="" src="https://media.geeksforgeeks.org/wp-content/uploads/20211103204646/graph1-300x300.png" style="float:left; height:300px; width:300px"></a><strong>
</strong></span>













<span style="font-size:18px">As you can see we have not taken the right subtree. </span></pre>

<p><strong><span style="font-size:18px">Y</span></strong><strong><span style="font-size:18px">our Task:</span></strong><br>
<span style="font-size:18px">This is a function problem. You don't have to take input. Just complete the <strong>function boundary()&nbsp;</strong>that takes the root node<strong>&nbsp;</strong>as input<strong>&nbsp;</strong>and returns an array containing&nbsp;the boundary values in anti-clockwise.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N).&nbsp;<br>
<strong>Expected Auxiliary Space:</strong> O(Height of the Tree).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 ≤ Number of nodes ≤ 10<sup>5</sup></span><br>
<span style="font-size:18px">1 ≤ Data of a node ≤ 10<sup>5</sup></span></p>
</div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Morgan Stanley</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Samsung</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>FactSet</code>&nbsp;<code>Hike</code>&nbsp;<code>Payu</code>&nbsp;<code>Kritikal Solutions</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;