<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get domain request
 */
class GetDomainRequest extends Model {
    protected $_name = [
        'domainId' => 'domain_id',
    ];
    public function validate() {
        Model::validateRequired('domainId', $this->domainId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetDomainRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        return $model;
    }
    /**
     * @description Domain ID
     * @example sz111
     * @var string
     */
    public $domainId;

}
