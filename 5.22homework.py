#need import numpy
def yakebi( x0, A, b, eps ):
    x1 = x0.copy( )
    times = 1
    while( True ):
        x0 = x1.copy( )
        for i in range( len(x0) ):
            x1[ i ] = b[ i ]
            for j in range( len( x0 ) ):
                if j == i:
                    continue
                
                x1[ i ] -= A[ i ][ j ] * x0[ j ]
                
            x1[ i ] = x1[ i ] / A[ i ][ i ]
            
        print( times, x1 )
        times += 1
        if max( abs( x1 - x0 ) ) <= eps:
            return x1


def gaosi( x0, A, b, eps ):
    x1 = x0.copy( )
    
    times = 1
    while( True ):
        for i in range( len( x1 ) ):
            x1[ i ] = b[ i ]
            for j in range( i ):
                x1[ i ] -= A[ i ][ j ] * x1[ j ]
            for j in range( i + 1, len( x1 ) ):
                x1[ i ] -= A[ i ][ j ] * x1[ j ]
            
            x1[ i ] /=  A[ i ][ i ]
        
        print( times, x1 )
        times = times + 1
        if max( abs( x1 - x0 ) ) <= eps :
            return x1
            
        x0 = x1.copy( )

if __name__ == '__main__':
    import numpy as np
    A = [ [5,2,1], [-1,4,2],[ 2,-3,10] ]
    b = [-12,20,3]
    x0 = [0,0,0]
    x0 = np.array( x0,dtype = float )
    A = np.array( A, dtype  = float )
    b = np.array( b, dtype = float )
