<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list storage file
 */
class ListStoreRequest extends Model {
    protected $_name = [
        'domainId' => 'domain_id',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ListStoreRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        return $model;
    }
    /**
     * @description domain_id
     * @example 10
     * @var string
     */
    public $domainId;

}
