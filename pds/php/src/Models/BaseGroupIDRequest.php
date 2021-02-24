<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseGroupIDRequest extends Model
{
    /**
     * @description group id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504793"
     *
     * @var string
     */
    public $groupId;

    /**
     * @description subdomain id
     *
     * @example "b38b5681bd964950ad8bc0f8ea504794"
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'groupId'     => 'group_id',
        'subdomainId' => 'subdomain_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->groupId) {
            $res['group_id'] = $this->groupId;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseGroupIDRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['group_id'])) {
            $model->groupId = $map['group_id'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
