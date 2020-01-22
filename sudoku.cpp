#include<cstdio>
#include<algorithm>
using namespace std;
const int n=9;
const int N=12;
int cnt=0,num[1<<N];
int w[N][N],x[N],y[N],z[N];
inline int F(int i,int j)
{
	return (i-1)/3*3+(j+2)/3;
}
inline void col(int i,int j,int s)
{
	x[i]^=s,y[j]^=s;
	z[F(i,j)]^=s;
}
void print()
{
	for(int i=1;i<=n;i++)
    {
    	for(int j=1;j<=n;j++)
    		printf("%d ",w[i][j]);
    	putchar('\n');
	}
}
void dfs()
{
    if (cnt==n*n) 
	{
		print();
		fclose(stdin),fclose(stdout);
		exit(0);
	}
    int u,v,val=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)if (!w[i][j])
        {
            int s=x[i]|y[j]|z[F(i,j)];
            if (num[s]<=num[val]) u=i,v=j,val=s;
        }
    for(int i=1;i<=n;i++)
        if ((val>>(i-1))&1^1)
        {
            w[u][v]=i,cnt++;
            col(u,v,1<<(i-1));
            dfs();
            col(u,v,1<<(i-1));
            w[u][v]=0,cnt--;
        }
}
int main()
{
	freopen("sudoku.in","r",stdin);
	freopen("sudoku.out","w",stdout);
    for(int i=1;i<=n;++i)
        for(int j=1;j<=n;++j) 
            scanf("%d",&w[i][j]);
    for(int s=0;s<(1<<n);++s)
        for(int i=1;i<=n;++i)
            num[s]+=(s>>(i-1))&1^1;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)if (w[i][j])
        {
        	cnt++;
        	if ((x[i]|y[j]|z[F(i,j)])&1<<(w[i][j]-1))
            {
                puts("0");
                return 0;
            }
        	col(i,j,1<<(w[i][j]-1));
        }
    dfs();
    fclose(stdin),fclose(stdout);
    return 0;
}
