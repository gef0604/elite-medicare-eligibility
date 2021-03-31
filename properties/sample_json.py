snf_sample_json = {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility04": {
                        "@value": "Medicare Part A"
                    },
                    "Eligibility01": {
                        "@value": "Benefit Description"
                    },
                    "Eligibility03": {
                        "@value": "Test Type"
                    }

                },
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "testnpi"
                        }
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
            }
        }
    }

hh_sample_json = {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Contains 'Home Health Care'"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "123123123123"
                        }
                    }
                },
                "Note":{
                    "Note01": {
                        "@value": "test status"
                    }
                }
            }
        }
    }

hospice_sample_json = {
        "Result": {
            "Section": {
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "123123123321"
                        }
                    }
                },
                "Service": {
                    "Service02": {
                        "@value": "25"
                    }
                },
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Hospice 123"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "Note": {
                    "Note01": {
                        "@value": "1"
                    }
                }
            }
        }
    }