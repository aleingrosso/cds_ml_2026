import matplotlib.pyplot as plt

color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

# some function for plotting used in Lecture4.1
def plotting_utility(E, wrange, ws, losses, plot_contours = True, minimizer = None, label="w"):
    plt.figure(figsize=(12,4))
    
    plt.subplot(131)
    if minimizer is not None:
        plt.plot(minimizer[0], minimizer[1], 'x')
    plt.imshow(E, extent=[wrange[0], wrange[-1], wrange[0], wrange[-1]], cmap="coolwarm", alpha=0.3, origin="lower")
    if plot_contours:
        plt.contour(E, levels=[1,4,9], extent=[wrange[0], wrange[-1], wrange[0], wrange[-1]])
    plt.plot(ws[0,0], ws[0,1], 'o', color="black")
    plt.plot(ws[:,0], ws[:,1], '.-', ms=5, color="gray")
    plt.xlabel(f"${label}_1$")
    plt.ylabel(f"${label}_2$")
    
    plt.subplot(132)
    plt.plot(ws[:,0], '.-', ms=5, label=f"${label}_1$")
    plt.plot(ws[:,1], '.-', ms=5, label=f"${label}_2$")
    plt.ylabel(f'{label}')
    plt.xlabel('t')
    plt.legend();

    plt.subplot(133)
    plt.plot(losses, '.-', ms=5, label=f"${label}_1$")
    plt.ylabel('loss')
    plt.xlabel('t')
    plt.legend();

    plt.tight_layout();