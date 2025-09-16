
class ClaimProviderConfiguration:
    def __init__(self, use_attending_provider_npi, use_supervising_provider_npi):
        self.use_attending_provider_npi = use_attending_provider_npi
        self.use_supervising_provider_npi = use_supervising_provider_npi

    def __str__(self):
        return f'ClaimProviderConfiguration:use_attending_provider_npi:{self.use_attending_provider_npi},use_supervising_provider_npi:{self.use_supervising_provider_npi}'


