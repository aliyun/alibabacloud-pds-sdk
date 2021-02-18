<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class GetBizCNameInfoRequest extends Model
{
    /**
     * @description cname type
     *
     * @example auth
     *
     * @var string
     */
    public $cnameType;

    /**
     * @description domain ID
     *
     * @example sz100
     *
     * @var string
     */
    public $domainId;

    /**
     * @description is vpc
     *
     * @example false
     *
     * @var bool
     */
    public $isVpc;
    protected $_name = [
        'cnameType' => 'cname_type',
        'domainId'  => 'domain_id',
        'isVpc'     => 'is_vpc',
    ];

    public function validate()
    {
        Model::validateRequired('cnameType', $this->cnameType, true);
        Model::validateRequired('domainId', $this->domainId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->cnameType) {
            $res['cname_type'] = $this->cnameType;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->isVpc) {
            $res['is_vpc'] = $this->isVpc;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetBizCNameInfoRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['cname_type'])) {
            $model->cnameType = $map['cname_type'];
        }
        if (isset($map['domain_id'])) {
            $model->domainId = $map['domain_id'];
        }
        if (isset($map['is_vpc'])) {
            $model->isVpc = $map['is_vpc'];
        }

        return $model;
    }
}
