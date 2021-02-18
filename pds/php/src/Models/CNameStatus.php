<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CNameStatus extends Model
{
    /**
     * @description binding state
     *
     * @example BINDING
     *
     * @var string
     */
    public $bingdingState;

    /**
     * @description legal state
     *
     * @example NORMAL
     *
     * @var string
     */
    public $legalState;

    /**
     * @description remark
     *
     * @example beian
     *
     * @var string
     */
    public $remark;
    protected $_name = [
        'bingdingState' => 'bingding_state',
        'legalState'    => 'legal_state',
        'remark'        => 'remark',
    ];

    public function validate()
    {
        Model::validateRequired('bingdingState', $this->bingdingState, true);
        Model::validateRequired('legalState', $this->legalState, true);
        Model::validateRequired('remark', $this->remark, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->bingdingState) {
            $res['bingding_state'] = $this->bingdingState;
        }
        if (null !== $this->legalState) {
            $res['legal_state'] = $this->legalState;
        }
        if (null !== $this->remark) {
            $res['remark'] = $this->remark;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CNameStatus
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['bingding_state'])) {
            $model->bingdingState = $map['bingding_state'];
        }
        if (isset($map['legal_state'])) {
            $model->legalState = $map['legal_state'];
        }
        if (isset($map['remark'])) {
            $model->remark = $map['remark'];
        }

        return $model;
    }
}
