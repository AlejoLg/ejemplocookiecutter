"""
Se declaran decorators para implementar ruido.
"""
import functools
from typing import Dict
from numpy.random import choice, random

def anadir_ruido(noise_probability : float, noise_distribution : Dict[str, float]):
    """Crea una función cuyos valores tienen una probabilidad de recibir ruido.

    Args:
        noise_probability (float): Porcentaje de probabilidad de ruido.
        noise_distribution (Dict[str, float]): Ruidos definidos con su respectiva probabilidad.
    """
    def inner_decorator(func):
        possible_noise_values = list(noise_distribution.keys())
        noise_value_probabilities = list(noise_distribution.values())
        @functools.wraps(func)
        def wrapper(*args):
            true_value = func(*args)
            if random() <= noise_probability: #ie con prob `noise_probability`
                vals, probs = exclude_true_value(possible_noise_values,
                                                noise_value_probabilities, true_value)
                return choice(vals, p=probs)
            return true_value
        return wrapper
    return inner_decorator


def exclude_true_value(possible_noise_values, noise_value_probabilities, true_value):
    """En funcion de una probabilidad, le agrega ruido al valor "True" de la función.

    Args:
        possible_noise_values (list): listas de  posibles ruidos a retornar.
        noise_value_probabilities (list): lista con las probabilidades de ruido.
        true_value (int): valor real de la función.
    """
    try:
        i = possible_noise_values.index(true_value)
        possible_noise_values = possible_noise_values[:i] + possible_noise_values[i+1:]
        noise_value_probabilities = noise_value_probabilities[:i] + noise_value_probabilities[i+1:]
        noise_probability = sum(noise_value_probabilities)
        noise_value_probabilities = [x/noise_probability for x in noise_value_probabilities]
    except ValueError:
        pass
    return possible_noise_values, noise_value_probabilities

if __name__ == "__main__":
    @anadir_ruido(0.5, {'ups!':0.7, 'UPS!':0.3})
    def funcion_de_ejemplo(value):
        """Recibo un valor y se duplica su contenido.

        Args:
            value (int): numero a duplicar.

        Returns:
            int: valor duplicado.
        """
        return 2*value
    for x in range(10):
        print(funcion_de_ejemplo(x))
