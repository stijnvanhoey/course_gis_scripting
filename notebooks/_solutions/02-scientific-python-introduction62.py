nete_bodem_subset[nete_bodem_subset <= 100000.] = 0
nete_bodem_subset[nete_bodem_subset > 100000.] = 1

plt.imshow(nete_bodem_subset)
plt.colorbar(shrink=0.8)