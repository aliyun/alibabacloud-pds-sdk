<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class LinkInfo extends Model {
    protected $_name = [
        'extra' => 'extra',
        'identity' => 'identity',
        'type' => 'type',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->extra) {
            $res['extra'] = $this->extra;
        }
        if (null !== $this->identity) {
            $res['identity'] = $this->identity;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return LinkInfo
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['extra'])){
            $model->extra = $map['extra'];
        }
        if(isset($map['identity'])){
            $model->identity = $map['identity'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
        }
        return $model;
    }
    /**
     * @description 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
     * @example 1
     * @var string
     */
    public $extra;

    /**
     * @description 当前用户已存在的登录标识
     * @example 15208345000
     * @var string
     */
    public $identity;

    /**
     * @description 当前用户已存在的登录方式
     * @example mobile
     * @var string
     */
    public $type;

}
