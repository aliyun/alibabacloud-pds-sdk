<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class VerifyCodeResponse extends Model {
    protected $_name = [
        'state' => 'state',
    ];
    public function validate() {
        Model::validateRequired('state', $this->state, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->state) {
            $res['state'] = $this->state;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return VerifyCodeResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['state'])){
            $model->state = $map['state'];
        }
        return $model;
    }
    /**
     * @description 修改密码的临时授权码
     * @example csjanwia
     * @var string
     */
    public $state;

}
