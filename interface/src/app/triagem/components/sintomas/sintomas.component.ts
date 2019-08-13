import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { TriagemService } from '../services/triagem.service';
import { SintomasModel } from '../models/components/sintomas.model';
import { FormBuilder, FormGroup, FormArray, FormControl, ValidatorFn } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-sintomas',
    templateUrl: './sintomas.component.html',
    styleUrls: ['./sintomas.component.scss']
  })
  export class SintomasComponent implements OnInit {
    constructor(
      private triagemService: TriagemService,
      private formBuilder: FormBuilder,
      private route: ActivatedRoute
    ) {
    }

    public listSintomas: SintomasModel[] = [];
    public form: FormGroup;

    @Input()
    idDiagnostico: number;
    
    @Output()
    isDiag: EventEmitter<boolean> = new EventEmitter(false);

    @Output()
    sintomas: EventEmitter<SintomasModel[]> = new EventEmitter(true);

    async ngOnInit() {
      this.form = this.formBuilder.group({
        sintomas: new FormArray([])
      });

      const response = await this.triagemService.ListarSintomas({idDiagnostico: this.idDiagnostico});
      response.data.forEach(sintoma => this.listSintomas.push({
        id: sintoma.idSintoma,
        descricao: sintoma.descricaoSintoma,
        checked: false
      }));
    }

    checkboxSintoma(Sintoma: SintomasModel){
      Sintoma.checked = !Sintoma.checked;
      console.log(this.listSintomas)
    }

    atualizaEstadoVital(){
      this.sintomas.emit(this.listSintomas);
    }

    renderDiagnostico(){
      this.isDiag.emit(true);
    }
  }