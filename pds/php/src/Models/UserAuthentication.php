<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class UserAuthentication extends Model
{
    /**
     * @description 认证类型
     *
     * @example mobile
     *
     * @var string
     */
    public $AuthenticationType;

    /**
     * @description 创建时间
     *
     * @example 1556163159820
     *
     * @var int
     */
    public $CreatedAt;

    /**
     * @description 详情
     *
     * @example {name:abc}
     *
     * @var string
     */
    public $Detail;

    /**
     * @description Domain ID
     *
     * @example 5000
     *
     * @var string
     */
    public $DomainID;

    /**
     * @description 唯一身份标识
     *
     * @example 15208345000
     *
     * @var string
     */
    public $Identity;

    /**
     * @description 最后登录时间
     *
     * @example 1556163159820
     *
     * @var int
     */
    public $LastLoginTime;

    /**
     * @description 状态
     *
     * @example normal
     *
     * @var string
     */
    public $Status;

    /**
     * @description 用户ID
     *
     * @example 00016a587b62b50003deea299a4f5b50
     *
     * @var string
     */
    public $UserID;

    /**
     * @description 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
     *
     * @example 1
     *
     * @var string
     */
    public $extra;

    /**
     * @description subdomain id
     *
     * @var string
     */
    public $subdomainId;
    protected $_name = [
        'AuthenticationType' => 'AuthenticationType',
        'CreatedAt'          => 'CreatedAt',
        'Detail'             => 'Detail',
        'DomainID'           => 'DomainID',
        'Identity'           => 'Identity',
        'LastLoginTime'      => 'LastLoginTime',
        'Status'             => 'Status',
        'UserID'             => 'UserID',
        'extra'              => 'extra',
        'subdomainId'        => 'subdomain_id',
    ];

    public function validate()
    {
        Model::validateRequired('AuthenticationType', $this->AuthenticationType, true);
        Model::validateRequired('CreatedAt', $this->CreatedAt, true);
        Model::validateRequired('Detail', $this->Detail, true);
        Model::validateRequired('DomainID', $this->DomainID, true);
        Model::validateRequired('Identity', $this->Identity, true);
        Model::validateRequired('LastLoginTime', $this->LastLoginTime, true);
        Model::validateRequired('Status', $this->Status, true);
        Model::validateRequired('UserID', $this->UserID, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->AuthenticationType) {
            $res['AuthenticationType'] = $this->AuthenticationType;
        }
        if (null !== $this->CreatedAt) {
            $res['CreatedAt'] = $this->CreatedAt;
        }
        if (null !== $this->Detail) {
            $res['Detail'] = $this->Detail;
        }
        if (null !== $this->DomainID) {
            $res['DomainID'] = $this->DomainID;
        }
        if (null !== $this->Identity) {
            $res['Identity'] = $this->Identity;
        }
        if (null !== $this->LastLoginTime) {
            $res['LastLoginTime'] = $this->LastLoginTime;
        }
        if (null !== $this->Status) {
            $res['Status'] = $this->Status;
        }
        if (null !== $this->UserID) {
            $res['UserID'] = $this->UserID;
        }
        if (null !== $this->extra) {
            $res['extra'] = $this->extra;
        }
        if (null !== $this->subdomainId) {
            $res['subdomain_id'] = $this->subdomainId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return UserAuthentication
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['AuthenticationType'])) {
            $model->AuthenticationType = $map['AuthenticationType'];
        }
        if (isset($map['CreatedAt'])) {
            $model->CreatedAt = $map['CreatedAt'];
        }
        if (isset($map['Detail'])) {
            $model->Detail = $map['Detail'];
        }
        if (isset($map['DomainID'])) {
            $model->DomainID = $map['DomainID'];
        }
        if (isset($map['Identity'])) {
            $model->Identity = $map['Identity'];
        }
        if (isset($map['LastLoginTime'])) {
            $model->LastLoginTime = $map['LastLoginTime'];
        }
        if (isset($map['Status'])) {
            $model->Status = $map['Status'];
        }
        if (isset($map['UserID'])) {
            $model->UserID = $map['UserID'];
        }
        if (isset($map['extra'])) {
            $model->extra = $map['extra'];
        }
        if (isset($map['subdomain_id'])) {
            $model->subdomainId = $map['subdomain_id'];
        }

        return $model;
    }
}
