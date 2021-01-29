<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class RemoveStoreRequest extends Model {
    protected $_name = [
        'domainId' => 'domain_id',
        'storeId' => 'store_id',
    ];
    public function validate() {
        Model::validateRequired('domainId', $this->domainId, true);
        Model::validateRequired('storeId', $this->storeId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->storeId) {
            $res['store_id'] = $this->storeId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return RemoveStoreRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        if(isset($map['store_id'])){
            $model->storeId = $map['store_id'];
        }
        return $model;
    }
    /**
     * @description domain ID
     * @example sz100
     * @var string
     */
    public $domainId;

    /**
     * @description store ID
     * @example cdjaksbwuiqbxuiassd
     * @var string
     */
    public $storeId;

}
