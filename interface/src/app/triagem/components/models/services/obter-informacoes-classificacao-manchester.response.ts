import { BaseResponse } from 'src/app/_shared/models/base.response';

export class ObterInformacoesClassificacaoManchesterResponse extends BaseResponse<ObterInformacoesClassificacaoManchesterModel>{
}

export class ObterInformacoesClassificacaoManchesterModel{
    public descricaoManchester: string;
    public tempoEspera: number;
    public corManchester: string;
}