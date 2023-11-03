#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int temp, max = 2;
	int min = 100000;

	while (n--) {
		scanf("%d", &temp);
		max = max < temp ? temp : max;
		min = min > temp ? temp : min;
	}
	printf("%d", max * min);

	return 0;
}