<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CreateSubdomainResponse extends Model
{
    /**
     * @description 用以唯一标识subdomain
     *
     * @example "c477c77a-aea8-413e-9ff0-30c24eeeae01"
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'subdomainId' => 'subdomain_id',
    ];

    public function validate()
    {
        Model::validateRequired('subdomainId', $this->subdomainId, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateSubdomainResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
