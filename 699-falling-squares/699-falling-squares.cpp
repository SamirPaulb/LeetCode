struct Node {
    int pos;
    int side;
    int height;
};
int placeNode(vector<struct Node*> &nlist, struct Node &n) {
    struct Node* max;
    bool max_is_defined = false;
    for(auto x : nlist) {
        if ((n.pos < x->pos + x->side) && (n.pos + n.side > x->pos)) {
            if (!max_is_defined) {
                max_is_defined = true;
                max = x;
            } else {
                if (max->height < x->height) {
                    max = x;
                }
            }
        }
    }
    if (max_is_defined) {
        n.height = n.side + max->height;
    } else {
        n.height = n.side;
    }
    nlist.push_back(&n);
    return n.height;
}

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        vector<struct Node *> v;
        vector<int> ans;
        int max = -1;
        for (auto x : positions) {
            struct Node* n = new struct Node;
            n->pos = x[0];
            n->side = x[1];
            int i = placeNode(v, *n);
            if (i > max) max = i;
            ans.push_back(max);
        }
        return ans;
    }
};