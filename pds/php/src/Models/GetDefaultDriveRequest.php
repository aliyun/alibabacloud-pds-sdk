<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Get default drive request.
 */
class GetDefaultDriveRequest extends Model
{
    public $headers;

    /**
     * @description Subdomain ID
     *
     * @example hz-123
     *
     * @var string
     */
    public $subdomainId;

    /**
     * @description 用户ID
     *
     * @example abc
     *
     * @var string
     */
    public $userId;
    protected $_name = [
        'subdomainId' => 'subdomain_id',
        'userId'      => 'user_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }
        if (null !== $this->userId) {
            $res['user_id'] = $this->userId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetDefaultDriveRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }
        if (isset($map['user_id'])) {
            $model->userId = $map['user_id'];
        }

        return $model;
    }
}
