//azhagu
#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;
int main()
{
    int n1;
    cin>>n1;
    if(n1==1){
            cout<<1;}
 else{   vector< pair<int,int> > vv;
    for(int i=0;i<n-1;i++){
        int lvl,node;
        cin>>lvl>>node;
        v.push_back(make_pair(lvl,node));
    }
    int l=vv.size();
    //cout<<v[l-1].first;
    vector< pair<int,int> > v1;
    for(int i=1;i<=vv[l-1].first;i++){
            vector< pair<int,int> > t;
        for(int j=0;j<v.size();j++){
            if(vv[j].first>i){break;}
            else if(vv[j].first==i){
            t.push_back(vv[j]);}
        }
            reverse(t.begin(),t.end());
            v1.insert(v1.end(),t.begin(),t.end());
    }
    for(int i=0;i<v1.size();i++){
            if(i==v1.size()-1){cout<<v1[i].first<<" "<<v1[i].second;}
       else{ cout<<v1[i].first<<" "<<v1[i].second<<endl;
    }}
}
    return 0;
}
