 $(document).ready(function()
    {

        carregando = "<h2><center><img src='/media/images/layout/ajax-loader.gif' /><br>confirmando...</center></h2>"

	var container_erro_endereco = $('#form_endereco_erros');

        $("#transacao_endereco_form").validate({
                errorContainer: container_erro_endereco,
		errorLabelContainer: $("ol", container_erro_endereco),
		wrapper: 'li',
		meta: "validate",

                rules: {
                    endereco: {
                        required: true
                    },
                    numero: {
                        required: true
                    },
                    bairro: {
                        required: true
                    },
                    cidade: {
                         required: true
                    },
                    estado: {
                         required: true
                    },
                    cep: {
                         required: true,
                         minlength: 9
                        
                    }
                },
                messages:
                {
                    endereco: "Digite seu endereço",
                    numero: "Digite o número da sua rua.",
                    bairro: "Digite seu bairro.",
                    cidade: "Digite sua cidade.",
                    estado: "Selecione seu estado.",
                    cep: "Digite seu cep corretamente."
                }
                 ,
                 submitHandler: function() {

                  var serializedForm = $("#transacao_endereco_form").serialize();
//                    $(".form_cartao").hide()
//                    $("#aux").html(carregando)
//                    $('#pagseguro').hide()
//                    $("#aux").fadeIn()
//                    $('.ou').hide()
                    $.ajax(
                    {
                        type: "POST",
                        url: "/confirma_endereco/",
                        data: serializedForm,
                        dataTypeString: "json",
                        success: function(retorno)
                        {
                             if(retorno.erro)
                                 {
                                     $("#form_endereco_erros").html(retorno.erro)
                                 }
                             if(retorno.endereco)
                                 {
                                     $("#cliente_bairro").val(retorno.endereco.bairro)
                                     $("#cliente_cidade").val(retorno.endereco.cidade)
                                     $("#cliente_end").val(retorno.endereco.endereco)
                                     $("#cliente_num").val(retorno.endereco.numero)
                                     $("#cliente_cep").val(retorno.endereco.cep)
                                     $("#cliente_uf").val(retorno.endereco.estado)
                                     $(".endereco").hide()
                                     $(".pagamento").fadeIn()
                                 }

//                            $("#aux").html(retorno)
//                            //$('#cartao').fadeIn()
//
//                            if (retorno.status == "capturada")
//                            {
//                                $("#aux").html("<h3 class='center'>Seu pagamento foi concluído com sucesso!</h3>");
//
////                                $("#saldoBid").html(retorno.saldoBids)
//
//                                //$("#step_confirmacao").addClass('active')
//                                //$("#step_pagamento").removeClass('active')
//                                //$('#formas_pagamento').hide()
//                                //$('#cartao').hide()
//                                //$('#alterarPagto').hide()
//                                //$.get("/confirmaPagamento/");
//
//                            }
//                            else
//                            {
//
//
//                                   $('#pagseguro').fadeIn()
//                                   $('.ou').fadeIn()
//                                   $("#aux").html("<h2 align='center'> <small> "+retorno.msg_erro+"<br>  Código do erro ("+retorno.codigo_erro+") <br> Se o problema persistir consulte sua administradora de cartão de crédito</small><br><a href='javascript:;' onclick='try_again()'>tente novamente</a>.</h2>");
//
//                            }
                        },
                        error:  function(retorno)
                        {
                               // $('#pagseguro').fadeIn()
                                //$('.ou').fadeIn()
                                //$("#aux").html("<h2 align='center'> <small> "+retorno.msg_erro+"<br> Código do erro ("+retorno.codigo_erro+") <br> Se o problema persistir consulte sua administradora de cartão de crédito</small><br><a href='javascript:;' onclick='try_again()'>tente novamente</a>.</h2>");
                               //$('#alterarPagto').fadeIn()
                        }
                    })
                }
              });

          


//               hiddenAll = function()
//               {
////                    $('#alterarPagto').hide()
////                    $('#formas_pagamento').hide()
////                    $('#pagseguro').hide()
////                    $('#boleto').hide()
////                    $('#cartao').hide()
////                    $('#transferencia').hide()
////                    $("#aux").hide()
////                    $('#confirmaBoleto').hide()
//               }



//               $(".alterarPagto").click(function()
//               {
//                   hiddenAll()
//                   $("#step_confirmacao").removeClass('active')
//                   $("#step_pagamento").addClass('active')
//                   $('#formas_pagamento').fadeIn()
//
//               })


//               $("#btn_pagseguro").click(function()
//               {
//                   //hiddenAll()
//                   $('#pagseguro').fadeIn()
//
//               })
//
//               $("#btn_visa").click(function()
//               {
//                   //hiddenAll()
//                   //$('#cartao').fadeIn()
//                   $('#alterarPagto').fadeIn()
//               })

//               $("#btn_boleto").click(function()
//               {
//                   window.open('/getBoleto','MDPAULISTA','navigator=0,menubar=1,location=0,resizable=0,width=680,height=805')
//                   hiddenAll()
//                   $("#step_confirmacao").addClass('active')
//                   $("#step_pagamento").removeClass('active')
//                   $('#alterarPagto').fadeIn()
//                   $('#confirmaBoleto').fadeIn()
//
//               })
//
//               $("#btn_tranferencia").click(function()
//               {
//                   hiddenAll()
//                   $("#step_confirmacao").addClass('active')
//                   $("#step_pagamento").removeClass('active')
//                   $('#alterarPagto').fadeIn()
//                   $.get("/deposito/");
//
//
//
//                   $('#transferencia').fadeIn()
//               })


    






        carregando = "<center><img src='/media/images/layout/ajax-loader.gif' /><br><h2>processando pagamento</h2></center>"

	var container = $('#form_erros');

        $("#transacao_form").validate({
                errorContainer: container,
		errorLabelContainer: $("ol", container),
		wrapper: 'li',
		meta: "validate",

                rules: {
                    bandeira: {
                        required: true
                    },
                    validade_mes: {
                        required: true
                    },
                    validade_ano: {
                        required: true
                    },
                    portador_codigo_seguranca: {
                        required: true
                    },
                    portador_numero: {
                        required: true
                    },
                    portador_nome_portador: {
                         required: true
                    }
                },
                messages:
                {
                    portador_codigo_seguranca: "Entre o código de segurança",
                    portador_nome_portador: "Entre com o seu nome como está no cartão",
                    portador_numero: "Entre com o número do cartão",
                    validade_mes: "Entre com o mês de vencimento.",
                    validade_ano: "Entre com o ano de vencimento.",
                    bandeira: "Escolha a bandeira do seu cartão de crédito."
                }
                 ,
                 submitHandler: function() {

                  var serializedForm = $("#transacao_form").serialize();
                    $(".form_cartao").hide()
                    $("#aux").html(carregando)
                    $('#pagseguro').hide()
                    $("#aux").fadeIn()
                    $('.ou').hide()
                    $.ajax(
                    {
                        type: "POST",
                        url: "/transacao/",
                        data: serializedForm,
                        success: function(retorno)
                        {

                            $("#aux").html(retorno)
                            //$('#cartao').fadeIn()

                            if (retorno.status == "capturada")
                            {
                                $("#aux").html("<h3 class='center'><b>"+retorno.mensagem+"</b></h3>");

                                $("#saldoBid").html(retorno.saldoBids)

                                //$("#step_confirmacao").addClass('active')
                                //$("#step_pagamento").removeClass('active')
                                //$('#formas_pagamento').hide()
                                //$('#cartao').hide()
                                //$('#alterarPagto').hide()
                                //$.get("/confirmaPagamento/");

                            }
                            else
                            {


                                   $('#pagseguro').fadeIn()
                                   $('.ou').fadeIn()
                                   $("#aux").html("<h2 align='center'> <small> <b>"+retorno.mensagem+"</b><br>  Código do erro ("+retorno.codigo+") <br> <small>Se o problema persistir consulte sua administradora de cartão de crédito</small></small><br><a href='javascript:;' onclick='try_again()'>tente novamente</a>.</h2>");

                            }
                        },
                        error:  function(retorno)
                        {
                                $('#pagseguro').fadeIn()
                                $('.ou').fadeIn()
                                $("#aux").html("<h2 align='center'> <small> <b>"+retorno.mensagem+"</b><br> Código do erro ("+retorno.codigo+") <br> <small>Se o problema persistir consulte sua administradora de cartão de crédito</small></small><br><a href='javascript:;' onclick='try_again()'>tente novamente</a>.</h2>");
                               //$('#alterarPagto').fadeIn()
                        }
                    })
                }
              });

            try_again = function()
            {

                $('#aux').hide()
                $('.form_cartao').fadeIn()

            }


//               hiddenAll = function()
//               {
////                    $('#alterarPagto').hide()
////                    $('#formas_pagamento').hide()
////                    $('#pagseguro').hide()
////                    $('#boleto').hide()
////                    $('#cartao').hide()
////                    $('#transferencia').hide()
////                    $("#aux").hide()
////                    $('#confirmaBoleto').hide()
//               }



//               $(".alterarPagto").click(function()
//               {
//                   hiddenAll()
//                   $("#step_confirmacao").removeClass('active')
//                   $("#step_pagamento").addClass('active')
//                   $('#formas_pagamento').fadeIn()
//
//               })


//               $("#btn_pagseguro").click(function()
//               {
//                   //hiddenAll()
//                   $('#pagseguro').fadeIn()
//
//               })
//
//               $("#btn_visa").click(function()
//               {
//                   //hiddenAll()
//                   //$('#cartao').fadeIn()
//                   $('#alterarPagto').fadeIn()
//               })

//               $("#btn_boleto").click(function()
//               {
//                   window.open('/getBoleto','MDPAULISTA','navigator=0,menubar=1,location=0,resizable=0,width=680,height=805')
//                   hiddenAll()
//                   $("#step_confirmacao").addClass('active')
//                   $("#step_pagamento").removeClass('active')
//                   $('#alterarPagto').fadeIn()
//                   $('#confirmaBoleto').fadeIn()
//
//               })
//
//               $("#btn_tranferencia").click(function()
//               {
//                   hiddenAll()
//                   $("#step_confirmacao").addClass('active')
//                   $("#step_pagamento").removeClass('active')
//                   $('#alterarPagto').fadeIn()
//                   $.get("/deposito/");
//
//
//
//                   $('#transferencia').fadeIn()
//               })


        })
